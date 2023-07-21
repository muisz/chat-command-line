import os
import sys
from enum import Enum

class Interface:
    def welcomePage(self):
        self.refreshPage()
        self.displayTitle("Welcome")
        print("[1] Login")
        print("[2] Register")
        print("[3] Exit")
        print()

        command = self.askUserCommand()
        if command == 1:
            self.loginPage()
        elif command == 2:
            self.registerPage()
        elif command == 3:
            sys.exit(0)
        else:
            self.welcomePage()
    
    def loginPage(self):
        self.refreshPage()
        self.displayTitle("Login")
        email = input("Email\t\t: ")
        password = input("Password\t: ")

        if email == "abdulmuis@email.com" and password == "testing":
            print()
            print("Login success, welcome Abdul Muis")
            self.wait()
            self.homePage()
        else:
            print()
            print("Invalid email or password")
            self.wait()
            self.loginPage()
    
    def registerPage(self):
        self.refreshPage()
        self.displayTitle("Register")

        name = input("Name\t\t: ")
        email = input("Email\t\t: ")
        password = input("Password\t: ")
        print()

        print("Account created")
        self.wait()
        self.loginPage()

    def homePage(self):
        self.refreshPage()
        self.displayTitle("Home")
        print("[1] Chat")
        print("[2] Profile")
        print("[3] Logout")
        print()

        command = self.askUserCommand()
        if command == 1:
            self.chatPage()
        elif command == 2:
            self.profilePage()
        elif command == 3:
            self.welcomePage()
        else:
            self.homePage()

    def chatPage(self):
        self.refreshPage()
        self.displayTitle("Chat")

        print("[1] Person 1....................................(3 new messages | 17:22)")
        print("[2] Person 2....................................(1 new messages | 17:22)")
        print("[3] Person 3...............................................(17 Jan 2022)")
        print("[4] New message")
        print("[5] Refresh")
        print("[6] Home page")
        print()

        command = self.askUserCommand()
        if command in (1, 2, 3):
            self.detailChatPage()
        elif command == 4:
            self.newMessagePage()
        elif command == 5:
            self.chatPage()
        elif command == 6:
            self.homePage()
        else:
            self.chatPage()

    def profilePage(self):
        self.refreshPage()
        self.displayTitle("Profile")
        print("Name\t: Muhamad Abdul Muis")
        print("Email\t: abdulmuis@email.com")
        print()
        self.wait()
        self.homePage()
    
    def newMessagePage(self):
        self.refreshPage()
        self.displayTitle("New message")

        destination_email = input("Destination email: ")
        print("Account found!")
        message = input("Your message: ")
        print("message sent!")
        self.wait()
        self.detailChatPage()
    
    def detailChatPage(self):
        self.refreshPage()
        self.displayTitle("Chat / Person 1", "active: 17.22")
        
        print("[you] hello")
        print("[person 1] hai")
        print()

        print("[1] Send message")
        print("[2] Refresh")
        print("[3] Chat page")
        print()

        command = self.askUserCommand()
        if command == 1:
            self.send_message()
        elif command == 2:
            self.detailChatPage()
        elif command == 3:
            self.chatPage()
        else:
            self.detailChatPage()
    
    def send_message(self):
        messages = input("Send message: ")
        print("message sent!")
        self.wait()
        self.detailChatPage()

    def displayTitle(self, name: str, attrs: str = ""):
        print("======================")
        print(name, end="\t\t")
        print(attrs)
        print("======================")
        print()

    def askUserCommand(self) -> int:
        command = input("Command: ")
        return int(command)

    def refreshPage(self):
        os.system("clear")

    def wait(self):
        input("Press any key to continue...")
