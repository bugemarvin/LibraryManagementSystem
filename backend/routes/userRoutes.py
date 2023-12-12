from controller.userController import UserController

class UserRoutes:
        def registerUser():
                return UserController.register()

        def loginUser():
                return UserController.login()

        def getUser():
                return UserController.getUsers()

        def logoutUser():
                return UserController.logout()