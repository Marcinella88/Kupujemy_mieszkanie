import numpy as np
import numpy_financial as npf
import matplotlib.pyplot as plt

value_apartment = 120000                                                                        # Wartość mieszkania obecnie
increase_value_apartment_per_year = 0.05                                                        # Wzrost ceny mieszkań w skali roku
increase_value_apartment_per_month = (1 + increase_value_apartment_per_year) ** (1/12) - 1      # Wzrost ceny mieszkań w skali miesiąca
rate = 0.12                                                                                     # Oprocentowanie lokat w skali roku
years = 5                                                                                       # Ilość lat
period_per_years = np.arange(years + 1)                                                         # Okres liczony w latach
period_per_month = np.arange(years*12 + 1)                                                      # Okres liczony w miesiącach


# 1.Ile będzie wynosiła orientacyjna cena mieszkania za 5 lat?

increase_value_apartment = np.round(value_apartment * (1 + increase_value_apartment_per_month) ** period_per_month, 2)
print(f"Orientacyjna cena mieszkania przy cenie początkowej {np.round(value_apartment,2)} PLN, przy założeniu wzrostu cen na poziomie {increase_value_apartment_per_year*100} % w skali roku to {np.round(np.max(increase_value_apartment),2)} PLN.")


# 2. Ile musisz wpłacać do banku każdego miesiąca, aby przy przedstawionej ofercie uzbierać na mieszkanie w ciągu 5 lat?

rate_month = rate / 12                                                                          # Oprocentowanie w skali miesiąca
month = years * 12                                                                              # Ilość miesięcy

constans_month_payment = - npf.pmt(rate_month, month, 0, fv=np.max(increase_value_apartment))
print(f"Aby uzbierać kwotę {np.round(np.max(increase_value_apartment),2)} PLN w ciągu {years}lat przy oprocentowaniu lokaty {rate*100} % należy miesięcznie odkładać kwotę: {np.round(constans_month_payment,2)} PLN.")

# Stwórz wykres przedstawiający, jak w interwałach miesięcznych zmieniać się będzie cena mieszkania (liniowy wzrost w całym okresie) oraz wartość twojej lokaty.

# Brakuje nam wartości wzrostu oszczędności na lokacie:

n = np.arange(month + 1)

increase_value_bank = constans_month_payment * ((1 + rate_month) ** n - 1) / rate_month
increase_value_bank = np.round(increase_value_bank, 2)

# Wykres:

plt.figure(figsize=(10, 6))
plt.plot(period_per_month, increase_value_apartment, label='Cena mieszkania')
plt.plot(n, increase_value_bank, label='Wartość oszczędności (lokata)')

plt.xlabel("Miesiące:")
plt.ylabel("Kwota (PLN):")
plt.title("Wzrost ceny mieszkania vs. kwota na lokacie")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()