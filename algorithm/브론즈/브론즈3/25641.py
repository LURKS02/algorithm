N = int(input())

st = input()

while(True):
    if st.count('s') == st.count('t'):
        print(st)
        break

    else:
        st = st[1:]