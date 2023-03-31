import pandas as pd
import numpy as np
import addon as ad

'''
Zakładamy, że dany jest układ równań Ax = b, gdzie A oznacza macierz współczynników stojących przy odpowiednich zmiennych,
natomiast b to wektor zawierający wynik dla każdego równania (czyli druga strona równości).

W przypadku metody Jacobiego wejściowa macierz współczynników stojących przy odpowienich zmiennych jest podzielona na 
trzy pomniejsze, zgodnie ze wzorem: A = L + D + U   

Wówczas:

* L to macierz zawierająca współczynniki tylko i wyłącznie pod główną przekątną
* D to macierz zawierająca współczynniki tylko i wyłącznie na głównej przekątnej
* U to macierz zawierająca współczynniki tylko i wyłącznie nad główną przekątną
'''


def divide_given_frame(data_frame):
    d_dataframe = data_frame.copy(deep=True)
    lu_dataframe = data_frame.copy(deep=True)

    for i in range(len(data_frame.index)):
        for j in range(len(data_frame.columns)):
            if i != j:
                d_dataframe.iloc[i, j] = 0
            else:
                lu_dataframe.iloc[i, j] = 0

    list_of_dataframes = [d_dataframe, lu_dataframe]
    return list_of_dataframes


'''
Funkcja obliczająca sumę iloczyn dwóch macierzy - w tej implementacji skorzystano z funkcji dot z biblioteki
pandas
'''


def dataframe_multiplication(data_frame_1, data_frame_2):
    result_dataframe = data_frame_1.dot(data_frame_2)
    return result_dataframe


'''
Funkcja obliczająca sumę elementów dwóch macierzy, stojących na tych samych indeksach - tzn. na tych 
samych pozycjach w pionie i poziomie.
'''


def sum_of_two_dataframes(data_frame_1, data_frame_2):
    result_dataframe = data_frame_1.values + data_frame_2.values
    return result_dataframe


'''
Funkcja obliczająca różnicę między elementami dwóch macierzy, stojącymi na tych samych indeksach - tzn. na tych 
samych pozycjach w pionie i poziomie.
'''


def diff_of_two_dataframes(df1, df2):
    result_df = df1.values - df2.values
    return result_df


'''
Funkcja oblicza dokładność jako różnicę między dwoma macierzami - w trakcie działania programu są tu podawane
wektory z rozwiązaniami układu równań, uzyskane w dwóch kolejnych iteracjach.
'''


def count_accuracy(df1, df2):
    results = df1.values - df2.values
    return max(abs(results))


'''
Funkcja wykorzysytwana do obliczenia macierzy odwrotnej do macierzy podanej tj. df 
'''


def correct_inverse(df):
    data_frame_inverse = pd.DataFrame(np.linalg.pinv(df.values), df.columns, df.index)
    data_frame_inverse.dot(df)
    return data_frame_inverse


'''
Funkcja wykorzystywana do sprawdzenia czy powstała w wyniku podania współczynników równań macierz jest 
zbieżna czy też nie - samo ustalenie opiera się na podaniu pierwotnej macierzy i wyliczeniu norm. 
'''


def check_convergence(start_df):
    list_of_sums_row = []
    sum_in_row = 0
    for i in range(len(start_df.index)):
        for j in range(len(start_df.columns)):
            sum_in_row += abs(start_df.iloc[i, j])
        list_of_sums_row.append(sum_in_row)
        sum_in_row = 0
    if max(list_of_sums_row) < 1:
        return True
    else:
        list_of_sums_column = []
        sum_in_column = 0
        for i in range(len(start_df.columns)):
            for j in range(len(start_df.index)):
                sum_in_column += abs(start_df.iloc[j, i])
            list_of_sums_column.append(sum_in_row)
            sum_in_column = 0
        if max(list_of_sums_row) < 1:
            return True
        else:
            list_of_sums_all = []
            sum_of_all_squared = 0
            for i in range(len(start_df.index)):
                for j in range(len(start_df.columns)):
                    sum_of_all_squared += abs(start_df.iloc[i, j]) ** 2
                list_of_sums_all.append(sum_of_all_squared)
                sum_of_all_squared = 0
            if max(list_of_sums_all) < 1:
                return True
            else:
                sum_of_all_exc_diag = 0
                for i in range(len(start_df.index)):
                    for j in range(len(start_df.columns)):
                        if j != i:
                            sum_of_all_exc_diag += abs(start_df[j][i])
                    if abs(start_df[i][i]) <= sum_of_all_exc_diag:
                        return False
                    sum_of_all_exc_diag = 0
                return True


'''
Funkcja znajdująca rozwiązanie dla podanego układu n równań linowych z n niewiadomymi. Jako parametry przyjmuje macierz 
współczynników (tj. coefficients), macierz wyrazów wolnych (czyli wyników równań, tj. result_vector), wybrany przez 
użytkownika warunek stopu (liczba iteracji / dokładność) i wartość dla danego kryterium (liczba iteracji / 
osiągnięcie podanej dokładności)
'''


def iterative_solving(coefficients, result_vector, criterion, value):
    if check_convergence(coefficients):
        list_of_dataframes = divide_given_frame(coefficients)
        dataframe_n = correct_inverse(list_of_dataframes[0])
        final_result = pd.DataFrame(index=range(len(result_vector.index)), columns=range(len(result_vector.columns)))
        temporary_df = pd.DataFrame(index=range(len(final_result.index)), columns=range(len(final_result.columns)))
        total_iterations = 0
        for i in range(len(final_result.index)):
            for j in range(len(final_result.columns)):
                final_result.iloc[i, j] = 0
                temporary_df.iloc[i, j] = 1
        if criterion == 1:
            while count_accuracy(final_result, temporary_df) > value and total_iterations < 1000:
                total_iterations += 1
                temporary_df = final_result
                final_result = dataframe_multiplication(dataframe_n,
                                                        diff_of_two_dataframes(result_vector, dataframe_multiplication(
                                                            list_of_dataframes[1], final_result)))
        elif criterion == 2:
            while value > 0:
                final_result = dataframe_multiplication(dataframe_n,
                                                        diff_of_two_dataframes(result_vector, dataframe_multiplication(
                                                            list_of_dataframes[1], final_result)))
                value -= 1
        if total_iterations < 1000:
            ad.new_line()
            for i in range(len(final_result)):
                print("Wartość x" + str(i + 1) + ": " + '{:.8f}'.format(final_result[0][i]))
        else:
            ad.new_line()
            print("Kryterium dokładności nie było w stanie wyznaczyć rozwiązania układu równań.")
    else:
        ad.new_line()
        print("Nie jest możliwe znalezienie rozwiązania, gdyż podana macierz współczynników nie jest zbieżna.")
