from common import find_search_term, list_of_searchable_fields, search_data


print("Welcome to Zendesk Search")
print("Type 'quit' to exit at any time, Press 'Enter' to continue\n")

quit = False

while (not quit):
    print("\nSelect search options:")
    print("* Press 1 to search Zendesk")
    print("* Press 2 to view a list of searchable fields")
    print("* Type 'quit' to exit\n\n")

    option = input()

    if option == "1":
        subOption = input(
            "Select 1) Users or 2) Tickets or 3) Organizations\n")

        if subOption == "1":
            search_term = input("Enter Search Term\n")

            if find_search_term(search_term, subOption):
                search_value = input("Enter Search value\n")
                search_data(search_term, search_value, subOption)
            else:
                print("Invalid Search Term\n")

        elif subOption == "2":
            search_term = input("Enter Search Term\n")

            if find_search_term(search_term, subOption):
                search_value = input("Enter Search value\n")
                search_data(search_term, search_value, subOption)
            else:
                print("Invalid Search Term\n")

        elif subOption == "3":
            search_term = input("Enter Search Term\n")

            if find_search_term(search_term, subOption):
                search_value = input("Enter Search value\n")
                search_data(search_term, search_value, subOption)
            else:
                print("Invalid Search Term\n")

        elif subOption == "quit":
            quit = True
            break
        else:
            print("Error: invalid option, try again\n")

    elif option == "2":
        list_of_searchable_fields()

    elif option == "quit":
        quit = True
        break

    else:
        print("Error: invalid option, try again\n")
