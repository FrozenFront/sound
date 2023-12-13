  import matplotlib.pyplot as plt
  import numpy as np
  #Функция для нахождения точной точки макимума
  def max_id_1(mas):
      maxa=max(mas)
      id = 0
      for i in range(len(mas)):
          if maxa <= mas[i]:
              id = i
      return id
  #Функция для нахождения максимума с погрешностью. Берет максимум, который подходит под погрешноть,
  #тот который стоит позже
  def max_id_2(mas):
      maxa = max(mas) -750
      id = 0
      for i in range(len(mas)):
          if maxa <= mas[i]:
              id = i
      return id
  
  def speed_for_data(Nu, id_a, id_b, dlin):
      v = dlin/((id_a-id_b)/Nu)
      return v
  
  def file_open(name):
      with open(name, 'r') as file:
          data = []
          for f in file:
              data.append(int(f.split()[0]))
      return data
  #Переменные
  Nu = 500000
  dlin = 1.158
  
  #Используемые файлы
  #Если будете использовать на своем устройстве то меняйте адреса
  air_0 = 'C:/Users/Павел/Desktop/Прога/Air/Test 4/data_0.txt'
  air_1 = 'C:/Users/Павел/Desktop/Прога/Air/Test 4/data_1.txt'
  co2_0 = 'C:/Users/Павел/Desktop/Прога/Air/CO2-1/data_0.txt'
  co2_1 = 'C:/Users/Павел/Desktop/Прога/Air/CO2-1/data_1.txt'
  
  #Открываем файлы
  data_0_air = file_open(air_0)
  data_1_air = file_open(air_1)
  data_0_co2 = file_open(co2_0)
  data_1_co2 = file_open(co2_1)
  
  id_0_air = max_id_1(data_0_air)
  id_1_air = max_id_1(data_1_air)
  v_air = speed_for_data(Nu, id_0_air, id_1_air, dlin)
  
  id_0_co2 = max_id_2(data_0_co2)
  id_1_co2 = max_id_2(data_1_co2)
  print(id_0_co2, id_1_co2)
  v_co2 = speed_for_data(Nu, id_0_co2, id_1_co2, dlin)
  
  print('Скорость для звука в сухом воздухе (влажность 32%')
  print(v_air)
  print('Скорость звука во влажном воздухе (влажность 100%')
  print(v_co2)

  Павел Лернер, сегодня в 15:14
  import matplotlib.pyplot as plt
  import numpy as np
  
  #функция для скорости от со2
  def gas_co2(v_p, T, co2_procent, const):
      #азот, кислород, аргон, углекислый газ
      gas_procent = [78.09, 20.95, 0.93, 0.03]
      gas_mol_m = [28.016, 32, 39.944, 44.01]
      h2o_mol = 18.016
      gas_procent[3] = co2_procent
      gas_procent[1] = const - co2_procent
      m = [5, 5, 3, 6]
      R = 8.31
      T += + 273
  
      p_w0 = 2.7276
      p_a =100
      p_w = v_p*p_w0
      c_h2o = p_w/p_a
  
      gas_procent[0] = gas_procent[0]*(1-c_h2o)
      gas_procent[2] = gas_procent[2]*(1-c_h2o)
  
      M=0
      for i in range(4):
          M += gas_procent[i]*gas_mol_m[i]/100000
      M += c_h2o*h2o_mol/1000
  
      a = 0
      b = 0
      for i in range(4):
          a += gas_mol_m[i]*gas_procent[i]*(m[i]+2)*R/200000
          b += gas_mol_m[i]*gas_procent[i]*m[i]*R/200000
      a += h2o_mol*c_h2o*8*R/2000
      b += h2o_mol * c_h2o * 6 * R / 2000
      gamma = a/b
  
      return (gamma*R*T/M)**0.5
  
  #функция для скоростей от темпeратуры и влажности
  def gas_h2o_T(v_p, T):
      #азот, кислород, аргон, углекислый газ
      gas_procent = [78.09, 20.95, 0.93, 0.03]
      gas_mol_m = [28.016, 32, 39.944, 44.01]
      h2o_mol = 18.016
      m = [5, 5, 3, 6]
      R = 8.31
      T += + 273
  
      p_w0 = 2.7276
      p_a =100
      p_w = v_p*p_w0
      c_h2o = p_w/p_a
  
      gas_procent[0] = gas_procent[0]*(1-c_h2o)
      gas_procent[2] = gas_procent[2]*(1-c_h2o)
  
      M=0
      for i in range(4):
          M += gas_procent[i]*gas_mol_m[i]/100000
      M += c_h2o * h2o_mol / 1000
  
      a = 0
      b = 0
      for i in range(4):
          a += gas_mol_m[i]*gas_procent[i]*(m[i]+2)*R/200000
          b += gas_mol_m[i]*gas_procent[i]*m[i]*R/200000
      a += h2o_mol * c_h2o * 8 * R / 2000
      b += h2o_mol * c_h2o * 6 * R / 2000
      gamma = a/b
  
      return (gamma*R*T/M)**0.5
  
  def grafics(x, y, a):
      x = np.array(x)
      y = np.array(y)
  
      fig, ax = plt.subplots()
      ax.set_title('Зависимость скорости звука от концентрации углекислого газа')
      ax.plot(x, y, label="Аналитическая зависимость",
              marker="", linestyle="-",
              color='r', linewidth=1)
  
      array_a_get = []
  
      ax.plot(0.04, a, label="Значение в воздухе: 345 [м/с], 0.05 [%]",
              marker="*", linestyle="",
              color='green', linewidth=1)
      ax.plot(2, 343.3, label="Значение при выдохе: 343.3 [м/с], 2 [%]",
              marker="*", linestyle="",
              color='green', linewidth=1)
      ax.grid(which = "major", linewidth = 1)
      ax.grid(which = "minor", linewidth = 0.2)
      ax.minorticks_on()
      plt.text(0, 341, 'Влажность составляет 31.1%\nТемпература составляет 22.6 градусов по Цельсию',
               bbox={"facecolor": "white",
                     "edgecolor": "black"}, size=7)
  
      plt.xlabel("Концентрация CO2 [%]", size=10)
      plt.ylabel("Скорость звука [м/с]", size=10)
      plt.legend()
      plt.show()
      # Сохраним график
      fig.savefig('SoundSpeedair.png', dpi=600)
  
  v_p = 0.32
  T = 22.6
  print('Скорость звука для идеального газа при заданной температуре и влажности')
  v=gas_h2o_T(v_p, T)
  print(v)
  
  mas_v_co2= [] #массив процентов со2
  mas_proc_co2 = [] #массив скоростей от со2
  const = 0.03 + 20.95
  for co2_procent in range(0, 500, 1):
      co2_procent = co2_procent/100
      mas_proc_co2.append(co2_procent)
      mas_v_co2.append(gas_co2(v_p, T, co2_procent, const))
  print(mas_v_co2)
  print(mas_proc_co2)
  
  grafics(mas_proc_co2, mas_v_co2, v)