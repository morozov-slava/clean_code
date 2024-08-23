# 3.1. Сделайте в своём коде три примера наглядных методов-фабрик.

from abc import ABC, abstractmethod 

# (1)
class DatabaseHandler(ABC): 
  @abstractmethod 
  def connect(self): 
    pass

  @abstractmethod 
  def close_connection(self):
    pass

  @abstractmethod 
  def select(self):
    pass


class PostgreHandler(DatabaseHandler):
  @abstractmethod 
  def connect(self): 
    pass
  
  @abstractmethod 
  def close_connection(self):
    pass

  @abstractmethod 
  def select(self):
    pass
  

# (2)



# 3.2. Если вы когда-нибудь использовали интерфейсы или абстрактные классы, напишите несколько примеров их правильного именования. 

DataValidator 
// Абстрактный класс для валидации различных данных с различной бизнес-логикой






