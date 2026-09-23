from models import Device, Master, ServiceOrder, SparePart


class AppleService:
  """Головна диспетчерська система сервісного центру."""

  def __init__(self, title: str):
    self.title = title
    self.parts = []  # Список об'єктів SparePart
    self.masters = []  # Список об'єктів Master
    self.orders = []  # Список об'єктів ServiceOrder
    self.logs = []  # Журнал системних повідомлень

  def add_part(self, part: SparePart):
    self.parts.append(part)

  def add_master(self, master: Master):
    self.masters.append(master)

  def add_order(self, order: ServiceOrder):
    self.orders.append(order)
    self.log(
        f"Прийнято замовлення #{order.order_id}: {order.device.model} від"
        f" {order.client_name}"
    )

  def log(self, message: str):
    self.logs.append(message)
    print(f"[СИСТЕМА] {message}")

  def process_all_orders(self):
    """Автоматичний цикл перевірки складу, призначення майстра та ремонту."""
    print(f"\n--- Запуск автоматичної обробки замовлень у {self.title} ---")

    # 1. Цикл for по списку замовлень
    for order in self.orders:
      dev = order.device

      if dev.is_fixed:
        continue

      print(f"\nОбробка замовлення #{order.order_id} ({dev.model})...")

      # 2. Пошук потрібної деталі на складі (цикл for + if)
      needed_part = None
      for part in self.parts:
        if part.part_name == dev.issue:
          needed_part = part
          break

      # 3. Пошук вільного майстра
      available_master = None
      for master in self.masters:
        if master.can_take_task():
          available_master = master
          break

      # 4. Перевірка умов через if / elif / else
      if needed_part is None or needed_part.stock_quantity <= 0:
        self.log(
            f"ПОМИЛКА: Немає деталі '{dev.issue}' на складі для замовлення"
            f" #{order.order_id}"
        )
      elif available_master is None:
        self.log(
            "ЧЕРГА: Усі інженери зайняті. Замовлення"
            f" #{order.order_id} очікує звільнення майстра."
        )
      else:
        # Успішне виконання ремонту
        available_master.assign_task()
        needed_part.take_one()
        dev.mark_as_fixed()
        order.set_cost(needed_part.price)
        available_master.complete_task()

        self.log(
            f"УСПІХ: Майстер {available_master.name} відремонтував {dev.model}."
            f" Чек: {order.cost:.2f} грн"
        )

  def show_report(self):
    """Підсумковий звіт роботи."""
    print("\n" + "=" * 45)
    print(f"ПІДСУМКОВИЙ ЗВІТ: {self.title}")
    print("=" * 45)

    print("Залишки на складі:")
    for part in self.parts:
      print(" - " + part.get_info())

    print("\nСтан майстрів:")
    for master in self.masters:
      print(" - " + master.get_info())

    print("\nВидані квитанції замовлень:")
    for order in self.orders:
      if order.device.is_fixed:
        order.print_receipt()
