class Device:
  """Пристрій клієнта (iPhone, Mac тощо)."""

  def __init__(self, model: str, serial_number: str, issue: str):
    self.model = model
    self.serial_number = serial_number
    self.issue = issue
    self.is_fixed = False

  def mark_as_fixed(self):
    """Метод зміни стану: позначає успішний ремонт."""
    self.is_fixed = True

  def get_status_info(self) -> str:
    """Метод отримання текстового стану пристрою."""
    status = "Відремонтовано" if self.is_fixed else "Потребує ремонту"
    return f"{self.model} (S/N: {self.serial_number}) | Несправність: {self.issue} | Стан: {status}"


class Master:
  """Інженер / майстер сервісного центру."""

  def __init__(self, name: str, max_load: int = 2):
    self.name = name
    self.active_tasks = 0
    self.max_load = max_load

  def can_take_task(self) -> bool:
    """Перевірка завантаженості майстра."""
    return self.active_tasks < self.max_load

  def assign_task(self):
    self.active_tasks += 1

  def complete_task(self):
    if self.active_tasks > 0:
      self.active_tasks -= 1

  def get_info(self) -> str:
    return (
        f"Майстер {self.name} - зайнятість: {self.active_tasks}/{self.max_load}"
    )


class SparePart:
  """Запчастина на складі."""

  def __init__(self, part_name: str, stock_quantity: int, price: float):
    self.part_name = part_name
    self.stock_quantity = stock_quantity
    self.price = price

  def take_one(self) -> bool:
    """Списання 1 деталі зі складу."""
    if self.stock_quantity > 0:
      self.stock_quantity -= 1
      return True
    return False

  def restock(self, qty: int):
    self.stock_quantity += qty

  def get_info(self) -> str:
    return f"{self.part_name}: {self.stock_quantity} шт. (Ціна: {self.price:.2f} грн)"


class ServiceOrder:
  """Квитанція замовлення клієнта."""

  def __init__(self, order_id: int, client_name: str, device: Device):
    self.order_id = order_id
    self.client_name = client_name
    self.device = device
    self.cost = 0.0

  def set_cost(self, part_price: float, labor_price: float = 600.0):
    """Розрахунок вартості: деталь + робота."""
    self.cost = part_price + labor_price

  def print_receipt(self):
    print(f"Квитанція #{self.order_id} | Клієнт: {self.client_name}")
    print(f"  Пристрій: {self.device.model} ({self.device.issue})")
    print(f"  Сума до сплати: {self.cost:.2f} грн")
