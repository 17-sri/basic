def main():
    try:
        a = int(input("Enter a number : "))
        print(a)
        return

    except Exception as e:
        print(e)
        return

    finally: # Here, without finally keyword print will not work
        print("Hey I'm inside finally block")

main()