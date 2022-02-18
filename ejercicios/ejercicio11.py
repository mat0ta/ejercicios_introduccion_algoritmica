horas_semana = 43
tarifa_por_hora = 13
paga_semanal = 35 * tarifa_por_hora

if horas_semana >= 44:
    paga_semanal = paga_semanal + ((horas_semana - 35) * (8 + (8 * 1.5)))
elif horas_semana >= 36 and horas_semana < 44:
    paga_semanal = paga_semanal + ((horas_semana - 35) * (8 + (8 * 1.25)))

print(paga_semanal)