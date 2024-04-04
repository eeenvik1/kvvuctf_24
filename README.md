# CTF

## reverse

### 1. Гуру реверса - 1000 

#### Платформа kvvuctf:

```
Описание

Разведчики перехватили аппаратуру шифрования противника, наши специалисты смогли восстановить [алгоритм](http://10.64.100.100/download/reverse_1000.py) проверки валидности ключа шифрования, кажется из него можно восстановить ключ. Помогите нам получить ключ шифрования, чтобы сорвать планы противника.

Задание

Необходимо получить флаг.
```
#### Writeup

[solve.py](https://github.com/eeenvik1/kvvuctf_24/blob/main/solve.py)

**Flag** - `kvvu{SMT_s0lv3r_1s_n00t_so_HArd}`



### 2. Полетное задание - 500 

#### Платформа kvvuctf:

```
Описание

Противник начал применять в своих дронах шифрование для защиты полетных заданий от анализа. Мы извлекли какую-то часть шифратора, возможно из нее можно извлечь что-то полезное.
Попробуйте проанализировать то, что у нас есть, пока наши аналитики извлекают оставшуюся часть шифратора

Задание

Необходимо получить флаг.
```
#### Writeup

[drone_solve.py](https://github.com/eeenvik1/kvvuctf_24/blob/main/drone_solv.py)

**Flag** - `kvvu{BR4V0_H3R0}`




## pwn

### 1. Уволенный сотрудник - 800

#### Платформа kvvuctf:

```
Описание

В организации есть файловый сервер - `10.64.x.110*`, развернутый на Ubuntu 20.04.1.
Администратор данного сервера уволился и никому не сказал пароль от суперпользователя. Бухгалтеру срочно нужно скачать файл с сервера. Логин и пароль бухгалтера: dirty:password123

`*10.64.x.110`, где х - номер вашей команды.

Задание

Необходимо повысить привилегии до суперпользователя и найти файл для бухгалтера.
```
#### Writeup

[exploit](https://github.com/worawit/CVE-2021-3156)

**Flag** - `kvvu_ctf{vuln3rabil1ties_r3@lly_c00l}`



### 2. Декриптор - 1000

#### Платформа kvvuctf:

```
### Описание

Центр кибермониторинга зафиксировал утечку данных на неконтролируемый хост.  
Расшифруйте и найдите данные, которые были похищены.

Специалистам удалось записать трафик.

### Задание

Необходимо получить флаг.

*Флаг в формате - kvvu{}*
```
#### Writeup

1) Открываем полученный pcap. Видим записанную сессию wireguard. Выписываем адреса взаимодействия. В описании была подсказка, что в записанном pcap был передан флаг.

2) Для того, чтобы найти флаг, сессию необходимо расшифровать. 
Ищем статьи на эту тему: https://blog.salrashid.dev/articles/2022/wireguard_wireshark/ видим, что для решения не хватает keylog файла.

3) сканируем участников взаимодействия. Видим, что на одном из них поднят wordpress. В изначальной версии уязвимые версии плагинов можно было найти через сканер. Для nuclei достаточно быстро была найдена нужная cve по тегам cve, wordpress. Позже была добавлена подсказка на главной, что использовался плагин backup. Находим в интернете последние cve c ним. Была заложена CVE-2023-6553. 

4) Эксплуатируем, получаем псевдошел. Далее задачи подняться не было, но вектора на всякий случай были заложены. Смотрим основные директории, где можно читать с правами пользователя www-data. Находим файл keylog.log в директории home. 

5) раскрываем сессию wireguard, смотрим, какие файлы были переданы. Находим флаг.

**Flag** - `kvvu{VPN_n0T_Hlid@en}`


## forensic

### 1. След от укола - 700

#### Платформа kvvuctf:

```
Описание

У нас произошла утечка, но мы никак не можем понять, какие именно данные у нас эксфильтровали.

Остался access.log веб-приложения, которое содержало Time-Based SQL-инъекцию. Данная инъекция была использована злоумышленником для доступа к СУБД и хищения флага.

Задание

Посмотреть лог и найти флаг.
```
#### Wirteup

Для решения задания нужно нормализовать записи из access.log и провести их анализ: соотнести нагрузку SQL-инъекции со временем ответа на запрос - так будет понятно какие нагрузки оказались правильными, что в итоге приведет нас к флагу. Скрипта под это решение нет - придется все делать самому.

**Flag** - `kvvuctf{t1m3_b4s3d_Sql1nJ3ct10n_h4s_b33n_3xpl01t3d!!!}`



### 2. Подозрительный трафик - 300

```
### Описание 

Во время одних из соревнований мы обнаружили передачу флага между участниками. 
Хорошо что мы записали трафик.
Сможете ли вы найти файл?

### Задание

Скачать файл и найти флаг.

```
#### Wtireup

На 1279 строке лежит флаг в открытом виде.

**Flag** - `flag{ocExwttcbN39GjWjJddijtkOKznMHNeYuTo3GwlcOS4edq_11}`


## crypto

### 1. Сломанное СМС - 200 ++

#### Платформа kvvuctf:

```
Описание

Разведка обнаружила шпиона, который отправлял информацию противнику. Вся отправляемая информация шифровалась, однако наши специалисты утверждают, что это точно не hex.

Задание

Перехваченное сообщение: `74 61 74 43 74 74 81 43 53 53 73 32 53 32 83 21 62 81`.

Необходимо расшифровать и получить флаг.

Полученое сообщение нужно обернуть в kvvu{}.
```
#### Writeup

[link](https://www.dcode.fr/multitap-abc-cipher)

**Flag** - `kvvu{SMSISSTILLRELEVANT}`





### 2. Плохая стеганография - 600 ++

#### Платформа kvvuctf:

```
Описание

На протяжении нескольких лет разведка перехватывает изоображения противника. Однако все изоображения изменены. Недавно удалось получить описание алгоритма изменения изображения:

"Разбитие изображения на квадраты 20 на 20 пикселей и постановка их в обратном порядке в новом изображении"

Одно из перехваченных сообщений.

Задание

Необходимо получить нормальное изображение.
```
#### Writeup

[create_flag.py](https://github.com/eeenvik1/kvvuctf_24/blob/main/create_flag.py)

**Flag** - `kvvu_ctf{n0t_A_str0ng_c1pher_1}`




### 3. Караул - 1000 

#### Платформа kvvuctf:

```
### Описание

Вы наткнулись на пост инопланетного караула. Немного последив за их работой вы насобирали некоторые данные.
Разгадайте пароль. Эти ребята ответа долго ждать не будут

### Задание

Разведайте секрет караула. Для попытки входа используйте nc `10.64.x+1.100:12346*` 

`*10.64.x+1.100`, где х - номер вашей команды.
```

#### Writeup

[solve_karaul.py](https://github.com/eeenvik1/kvvuctf_24/blob/main/solve_karaul.py)

**Flag** - `KVVUCTF{S@miY_dL1nNiY_In$strUktaG3_v_Tvo3i_Zhizni}`







## web

### 1. Подпись командира - 300 

#### Платформа kvvuctf:

```
Описание

Дневальный не пускает в комнату досуга посмотреть на флаг.

Говорит, что ему нужна подпись командира, чтобы пропустить.

Подключаться к `http://10.64.x.100:5000/ *`

`*10.64.x.100:5000`, где х - номер вашей команды.

Задание

Получить флаг.
```

#### Writeup

Для решения необходимо сбрутить ключ сессий по rockyou утилитой flask-unsign, после чего подписать свой токен и получить флаг.

**Flag** - `kvvuctf{w3ak_s3cr3t_k3y_1n_s3ss10n_n0w}`




### 2. Государственный контракт - 400

#### Платформа kvvuctf:

```
Описание

Нам удалось получить доступ к площадке государственных закупок не дружественного государства - http://10.64.x.100:3000/ *. Web-приложение позволяет просматривать объекты закупок с описанием и ценами. Разведка докладывает, что где-то в приложении можно посмотреть контракт (contract) на закупку .

*10.64.x.100:3000, где х - номер вашей команды.

Задание

Найти контракт на закупку и его номер.
```

#### Writeup

1. sql-injection. Получаем логин и пароль админа.
http://ip:3000/product/25%20UNION%20SELECT%20NULL,username,NULL,password%20from%20users

2. Логинимся, получаем jwt токен 
http://ip:3000/login
admin
fs3!m4mf3kf4

3. Авторизируемся используя jwt token
header: 
Authorization Bearer jwt_token

get http://ip:3000/contract


4. Получаем флаг.
Флагом является номер контракта на закупку. Флаг закодирован в base64.

**Flag** - `kvvu{it_!s_number_of_top_$ecret_contract_pwn}`


### 3. Ракетная атака - 500 

#### Платформа kvvuctf:

```
### Описание

Разведка доложила о том, что всё высшее руководство врага собралось в секретном пункте сбора. 
Адрес этого пункта не знают даже враги, так как координаты секретного центра передаются в случае эвакуации с объекта в случае его полного разрушения.
Нам удалось получить доступ к вражескому центру координации ракетных ударов. В приложении враг дает команды на атаку наших городов и отслеживает результаты атаки. Наши ракеты не достают до центра координации, однако были замечены прецеденты, когда враг ставил для целей не верные координаты и проводил атаки по своим войскам. Возможно мы сможем использовать это себе на пользу.

Вражеский центр координации - `http://10.64.x+1.100:4000/*`

`*10.64.x+1.100:4000`, где х - номер вашей команды.

### Задание

Узнать координаты секретного пункта сбора чтобы получить флаг.
```

#### Writeup

1. Просканировать диапазон
POST http://10.64.1.100:4000/target/{1__1000}

2. Выявить объекты.
id: 578,
id: 876,
id: 922

3. Для любого из объектов задать координаты центра управления рокетными ударами
POST http://localhost:4000/target/578

 {
  "coordinates": "404, -300"
 }

4. Атаковать объект которому вы назначали координаты 10 раз, что бы суммарный урон центру оказался больше 100

**Flag** - `kvvu{secret_place_coordinates_233_43}`


## misc

### 1.Обменник - 300 

#### Платформа kvvuctf:

```
### Описание

Единая система государственных закупок предоставила доступ к своей обменной бирже.
Чтобы получить ВИП-флаг, необходимо иметь на балансе более 1000 рублей.

Для доступа к системе использовать: `nc 10.64.x+1.100:12345*`

nc 10.64.x+1.100:12345*,  где х - номер вашей команды

### Задание

Получить флаг.


*Флаг в формате - kvvuctf*
```
#### Writeup

Подключаемся с помощью netcat/ncat к сервису. Видим доступные операции.

У нас есть 100 долларов. Меняем 4, видим, что обменный курс 3 рубля на один доллар. 

Проверяем, если ли уязвимость связанная с округлением. Для этого меняем 5 рублей, затем еще раз 5, и потом 2. Видим, что прибавилась один цент. Повторяем операцию, пока не будет 110.

**Flag** - `kvvuctf{DenGy_not_m2ln_1n_L3Fe}`

