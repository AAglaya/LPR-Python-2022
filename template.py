def task1():
    n, m = map(int, input().split())
    ans = n ** 2 + m ** 2
    return ans

def task2():
    s = input()
    num = 0
    for i in range(len(s)):
        if ord(s[i]) >= 65 and ord(s[i]) <= 90:
            num += 1
    return num

def task3():
    list = list(map(str, input().split()))
    num = 0
    for i in range(len(list)):
        if list[i][:3] == 'Abo':
            num += 1
    return num

def task4(generator):
    a = (filter(lambda x: x % 2 != 0, generator))
    return a

def task5(list_of_smth):
    a = list_of_smth[4:-1:3]
    ans = a[::-1]
    return ans

def task6(list1, list2, list3, list4):
    set1 = set(list1).union(set(list4))
    set2 = set(list2).union(set(list3))
    ans = set1.intersection(set2)
    return ans

def task7():
    np.random.seed(2)
    a = np.random.randint(0, 50, (7, 7))
    print(a)
    b = np.delete(a, 5, axis=0)
    b = np.delete(b, 5, axis=1)
    det = np.linalg.det(b)
    return a

def task8(f, min_x, max_x, N, min_y, max_y):
    x = np.linspace(min_x, max_x, N)
    f = np.sin(x)
    plt.plot(x, f, color='b', label='k--')
    dx = x[1] - x[0]
    plt.plot(x, np.gradient(f, dx), color='r', label='k--')
    plt.ylim(min_y, max_y)
    plt.grid()
    plt.xscale('log')
    plt.savefig('function.pdf')
    plt.show()


def task9(data, x_array, y_array, threshold):
    data2 = data.reshape(len(data) * 2)
    plt.hist(data2, "auto")
    plt.savefig('histograms_0.jpg')

    plt.show()

def task10(list_of_smth, n):
    ans = []

    def foo(x):
        a = 1
        m = min(x + n + 1, len(list_of_smth))
        for i in range(x, m):
            a *= list_of_smth[i]
        return a ** (1 / n)

    for x in map(foo, range(len(list_of_smth))):
        ans.append(x)

    return ans

def task11(filename="infile.csv"):
    df = pd.read_csv(filename)

    for name in ['x', 'y', 'x_err', 'y_err']:
        mask = pd.isna(df[name])
        print(len(list(df[mask][name].index)))

    mask = pd.isna(df['x'])
    a = list(df[mask]['x'].index)

    for i in a:
        df['x'].iloc[i] = (df['x'].iloc[i - 1] + df['x'].iloc[i + 1]) / 2

    df['x_err'].fillna(df['x_err'].mean(), inplace=True)

    mask = pd.isna(df['y'])
    l = list(df[mask]['y'].index)
    df = df.drop(index=l)
    mask = pd.isna(df['y_err'])
    l = list(df[mask]['y_err'].index)
    df = df.drop(index=l)

    print(df)

    plt.plot(df['x'], df['y'])
    plt.errorbar(df['x'], df['y'], yerr=df['y_err'], xerr=df['x_err'], fmt='.', color='tab:orange', label='Кресты')
    plt.grid()
    plt.minorticks_on()
    plt.savefig('dataframe.pdf')
    plt.show()

def task12(filename="video-games.csv"):
    # TODO: ...
