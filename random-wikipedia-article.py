import wikipedia, webbrowser


def get_article():
    title = wikipedia.random(1)

    link = wikipedia.page(title)


    user = input("Would you like to go through the topic: %s ?(Y/N/Q)" %title).lower().strip()

    if (user == "y" or user == "yes"):
        print("\n Summary:\n")
        print(link.summary)
        choice = input("\nWould you like to open this article in browser?(Y/N)").lower().strip()
        print("\n")
        if (choice == "y" or choice == "yes"):
            webbrowser.open(link.url, new=2)
        else:
            get_article()
        exit(0)

    else:
       print("\n")
       if(user == "n" or user == "no"):
         get_article()
       else:
         exit(0)

if __name__ == "__main__":
    get_article()
