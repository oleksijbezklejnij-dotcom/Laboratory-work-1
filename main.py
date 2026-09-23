from models import Device, Master, ServiceOrder, SparePart
from service import AppleService


def main():
  # 1. Ініціалізація головного сервісу
  hub = AppleService("iStore Lab & Repair")

  # 2. Додаємо деталі на склад
  hub.add_part(SparePart("Заміна батареї", stock_quantity=2, price=2800.0))
  hub.add_part(SparePart("Заміна дисплея OLED", stock_quantity=1, price=5400.0))
  hub.add_part(
      SparePart("Заміна камери", stock_quantity=0, price=3200.0)
  )  # Деталь відсутня для перевірки if/else

  # 3. Додаємо майстрів
  hub.add_master(Master("Олексій", max_load=2))
  hub.add_master(Master("Артем", max_load=1))

  # 4. Реєструємо пристрої та створюємо замовлення
  d1 = Device("iPhone 15 Pro", "SN-40291", "Заміна батареї")
  d2 = Device("iPhone 14", "SN-88312", "Заміна дисплея OLED")
  d3 = Device("iPhone 13 Pro", "SN-10294", "Заміна камери")

  hub.add_order(ServiceOrder(101, "Артем", d1))
  hub.add_order(ServiceOrder(102, "Вікторія", d2))
  hub.add_order(ServiceOrder(103, "Максим", d3))

  # 5. Запуск автоматичної обробки
  hub.process_all_orders()

  # 6. Виведення звіту
  hub.show_report()


if __name__ == "__main__":
  main()
