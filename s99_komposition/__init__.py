from dataclasses import dataclass
class User:   
    def __init__(self,user,password):
        self.user = user
        self.password = password
      
    def __repr__(self):
        password_encrypted = list()
        i = len(self.password)
        c = 0     
        while c < i:
            sträng = ''.join(map(str, password_encrypted))
            password_encrypted.append("**")
            c += 1 
        output = f"Användarnamn: {self.user}\nLösenord:{sträng}"
        return output

@dataclass(init=True,repr=True)
class UserInformation(User):
    favorite_activites : str
    favorite_foods : str
    parents: bool
    


user_1 = User("Kalle", "Pannkakor123*")
user_1.favorite_activites = "Gymma"
user_1.favorite_foods = "spaghetti"
user_1.parents = True


import unittest
class TestUserClass(unittest.TestCase,User):
    def __init__(self,user,password):
        super().__init__(user,password)
    def user_password_length(self):
        self.assertTrue(len(password)>21)
    def symbols_in_username(self):
        invalid_symbols = ["*","-", "<", "!", "+"]
        index_of_user = [i for i in user_1.user]
        invalid = ''.join(map(str, invalid_symbols))
        assert invalid_symbols not in index_of_user, f"you are using invalid symbols:{invalid}"



