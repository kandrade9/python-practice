def main():
    greeting = input("Greeting: ").lower()
    bank(greeting)

def bank(word):
    if "hello" in word:
        print("$0")
    elif "h" in word:
        print("$20")
    else:
        print("100")

main()
