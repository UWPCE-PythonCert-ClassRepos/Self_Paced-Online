def gas_prices(usgas):
    answer = usgas / 3.78 * 1.3
    answer = round(answer, 2)
    answer = str(answer)
    return ("CAD $" + answer)