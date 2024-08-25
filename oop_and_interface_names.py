# 3.1. Сделайте в своём коде три примера наглядных методов-фабрик.

from abc import ABC, abstractmethod 


# (1)
# Класс-фабрика для создания интерфейса для различных коннекторов в базам данных
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
  def connect(self): 
    pass
  
  def close_connection(self):
    pass

  def select(self):
    pass

# (2)
# Класс-фабрика для создания интерфейса для оптимизации гиперпараметров различных моделей с помощью библиотеки Optuna
class OptunaOptimizer(ABC):
  @abstractmethod 
  def create_optimizer(self): 
    pass

  @abstractmethod 
  def objective(self): 
    pass


class LgbClassifierOptimizer(OptunaOptimizer):
  def create_optimizer(self): 
    pass

  def objective(self): 
    pass


# (3) 
# Класс-фабрика для создания интерфейса для различных моделей кластеризации
class ClusteringModel(ABC):
  @abstractmethod 
  def fit(self): 
    pass

  @abstractmethod 
  def predict(self): 
    pass
    
  @abstractmethod
  def get_labels(self):
    pass

class KMeans(ClusteringModel):
  def fit(self): 
    pass

  def predict(self): 
    pass
    
  def get_labels(self):
    pass


# 3.2. Если вы когда-нибудь использовали интерфейсы или абстрактные классы, напишите несколько примеров их правильного именования. 

# Абстрактный класс для валидации данных на соответствие различной бизнес-логикой
DataValidator 

# Абстрактный класс для выгрузки признаков для моделей определённого типа
FeaturesExtractor

# Абстрактный класс для разработки структуры отчётов по выручке
RevenueReportTemplater

# Абстрактный класс для различных методов обработки выбросов в данных
OutliersDetector


