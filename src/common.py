import json


def find_search_term(search_term, subOption):

    if subOption == "1":
        with open('resources/users.json') as jsondata:
            users_data = json.load(jsondata)

        if search_term in users_data[0].keys():
            return True
        else:
            return False

    elif subOption == "2":
        with open('resources/tickets.json') as jsondata:
            tickets_data = json.load(jsondata)

        if search_term in tickets_data[0].keys():
            return True
        else:
            return False

    elif subOption == "3":
        with open('resources/organizations.json') as jsondata:
            organizations_data = json.load(jsondata)

        if search_term in organizations_data[0].keys():
            return True
        else:
            return False


def list_of_searchable_fields():

    with open('resources/users.json') as jsondata:
        users_data = json.load(jsondata)

    with open('resources/tickets.json') as jsondata:
        tickets_data = json.load(jsondata)

    with open('resources/organizations.json') as jsondata:
        organizations_data = json.load(jsondata)

    print("--------------------------------------------")
    print("Search Users with")
    for k in users_data[0].keys():
        print(k)

    print("\n")
    print("--------------------------------------------")
    print("Search Tickets with")
    for k in tickets_data[0].keys():
        print(k)

    print("\n")
    print("--------------------------------------------")
    print("Search organizations with")
    for k in organizations_data[0].keys():
        print(k)

    print("\n\n")


def search_data(search_term, search_value, subOption):

    if subOption == "1":
        with open('resources/users.json') as jsondata:
            users_data = json.load(jsondata)

        users_list = list()
        for i in users_data:
            if str(i.get(search_term)) == search_value:
                users_list.append(i)

        if len(users_list) > 0:
            for user in users_list:
                print("------------------------------------------------------")
                for k, v in user.items():
                    print(k, "\t\t\t", v)
                print("------------------------------------------------------")
        else:
            print("No data Found\n\n")

    elif subOption == "2":
        with open('resources/tickets.json') as jsondata:
            tickets_data = json.load(jsondata)

        tickets_list = list()
        for i in tickets_data:
            if str(i.get(search_term)) == search_value:
                tickets_list.append(i)

        if len(tickets_list) > 0:
            for ticket in tickets_list:
                print("------------------------------------------------------")
                for k, v in ticket.items():
                    print(k, "\t\t\t", v)
                print("------------------------------------------------------")
        else:
            print("No data Found\n\n")

    elif subOption == "3":
        with open('resources/organizations.json') as jsondata:
            organizations_data = json.load(jsondata)

        organizations_list = list()
        for i in organizations_data:
            if str(i.get(search_term)) == search_value:
                organizations_list.append(i)

        if len(organizations_list) > 0:
            for org in organizations_list:
                print("------------------------------------------------------")
                for k, v in org.items():
                    print(k, "\t\t\t", v)
                print("------------------------------------------------------")
        else:
            print("No data Found\n\n")
