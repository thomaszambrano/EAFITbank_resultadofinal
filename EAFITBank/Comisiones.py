class Comisiones:

    def calcular_deuda_total(self, grupo, meses):
        deuda_actual = grupo.obtener_prestamo()
        if deuda_actual > 0:
            valor_por_mes = deuda_actual / grupo.obtener_meses()
            valor_a_pagar = valor_por_mes * meses
            intereses = valor_a_pagar * (3 / 100) * meses
            total_a_pagar = valor_a_pagar + intereses
            return total_a_pagar, valor_a_pagar
    
    def comision_transacciones(self, valor_transaccion):
        comision = valor_transaccion * 0.001  # 0.1% = 0.001
        return comision
