class Player:
  import json
  data_file = r"C:\Users\rouge\Documents\sourceCodes\project\Quiz_app\app\data\players.json"
  def __init__(self) -> None:
    pass
  
  def check_player(self,name):
    player_exists = None
    file_location = open(self.data_file)
    for player in file_location:
      if player["player_name"] == name: # type: ignore
        player_exists = True
        file_location.close()
        break
        
      else:
        player_exists = False
        file_location.close()
        break
    if player_exists == True:
      return False
    else:
      return True
    #if False is returned then the player already exists else if it returns True means player does not exist
      
  def create_new_player(self,name):
    validation = self.check_player(name)
    file_location = self.data_file
    if validation == True:
      player_data = {}
      player_data["player_name"] = name

    else:
      return False
    
sam = Player()
print(sam.create_new_player("Manasseh"))