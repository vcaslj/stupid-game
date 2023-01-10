from random import choice as ch
from random import randrange as rr
from random import shuffle as sh
from random import randint as ran

herous_powers = {'Superman': '100', 'Batman': '60', 'Thor': '90', 'Hulk': '80', 'Captain America': '70', 'Spider-Man': '75', 'Wolverine': '80', 'Green Lantern': '85', 'Flash': '80', 'Professor X': '70', 'Wonder Woman': '90', 'Iron Man': '70', 'Mister Fantastic': '75', 'Deadpool': '60', 'Aquaman': '80', 'Dr. Stephen Vincent Strange': '80'}

herous_abilitys = {'Superman': ['Неуязвимость', 'Сверхчеловеческие сила', 'Сверхчеловеческие cкорость', 'Сверхчеловеческие зрение и слух', 'Морозное дыхание', 'Тепловое зрение', 'Рентгеновское зрение', 'Полёт'],
                   'Batman': ['Интеллект на уровне гения', 'Обширные познания во многих областях науки', 'Гениальный стратег', 'Лучший в мире детектив', 'Пик физического развития человека', 'Мастер множества боевых искусств мира', 'Мастер маскировки и скрытности', 'Огромная сила воли', 'Большие финансовые возможности', 'Доступ к высокотехнологичным устройствам', 'Проворство и ловкость', 'Мастер давления и запугивания', 'Умелый фехтовальщик', 'Меткий стрелок', 'Мастерство побегов', 'Эксперт по обращению с различным оружием'],
                   'Thor': ['Физиология Асгардца', 'Скорость', 'Выносливость', 'Ловкость', 'Стойкость', 'Иммунитет ко всем ядам, болезням, токсинам', 'Неуязвимость', 'Регенерация', 'Перерождение', 'Удлинённый период жизни', 'Замедленное старение', 'Контроль над погодой', 'Полёт', 'Способность призывать молнии'],
                   'Hulk': ['Неизмеримая физическая сила, скорость, прыжки,выносливость, ловкость и стойкость', 'Иммунитет ко всем ядам, болезням и токсинам', 'Исцеление', 'Интеллект уровня гения в определённых инкарнациях', 'Поглощение радиации и тёмной магии', 'Математическое видение мира', 'Безграничный лимит ярости', 'Устойчивость к телепатии', 'Реактивная адаптация', 'Метафорическое бессмертие', 'Самообеспечение', 'Наводящее чувство', 'Огнеупорность'],
                   'Captain America': ['Пик человеческих сил', 'Превосходная физическая форма', 'Ускоренный метаболизм', 'Выносливость развита до предела', 'Мастер множества боевых искусств', 'Великолепные акробатические данные', 'Превосходный тактик, стратег и полевой командир', 'Лидерские качества', 'Шпионские навыки', 'Мастерство скрытности', 'Лучший рукопашный боец мира', 'Иммунитет ко всем болезням', 'Ускоренная регенерация', 'Прочность', 'Высокий болевой порог', 'Замедленное старение', 'Рефлексы ускорены до предела', 'Высокая скорость'],
                   'Spider-Man': ['Сверхчеловеческие рефлексы, сила, скорость, прыжки в высоту и в длину 10 метров и ловкость', 'Развит вестибулярный аппарат', 'Ускоренный метаболизм', 'Способность прилипать к твёрдым поверхностям', '«Паучье чутьё»', 'Ускоренное заживление ран', 'Владение боевыми искусствами', 'Гениальный интеллект (IQ - 250)', 'Ночное зрение (не всегда)'],
                   'Wolverine': ['Исцеляющий фактор', 'Иммунитет ко всем ядам, болезням и токсинам','Замедление старения', 'Сопротивление усталости и телепатии', 'Выдвижные костяные когти', 'Сверхчеловеческие слух, вкус и сверхчеловеческое зрение, осязание и обоняние', 'Сверхчеловеческая сила, скорость, ловкость, реакция, выносливость и стойкость', 'Эмпатия к животным', 'Опытный следопыт', 'Высокий уровень интеллекта', 'Мастер боевых искусств', 'Эксперт по лидерству, оружию, компьютерам и и транспортным средствам', 'Опытный убийца', 'Полиглот'],
                   'Green Lantern': ['Способность с помощью силы Кольца создавать энергетические объекты и управлять ими'],
                   'Flash': ['Способность передвигаться со сверхсветовой скоростью', 'Сверхчеловеческая сила, скорость, стойкость, выносливость', 'Возможность перемещения во времени и параллельных мирах', 'Контроль тела на молекулярном уровне', 'Фазировка сквозь предметы', 'Поле Спидфорса', 'Ускоренное мышление', 'Сверхчеловеческие рефлексы', 'Ускоренная регенерация', 'Способность, используя сверхбыстрые вибрации, убивать с одного удара', 'Кража скорости других спидстеров', 'Метание молний', 'Создание временных реликтов-двойников', 'Манипуляция энергией вселенной'],
                   'Professor X': ['Гениальный интеллект', 'Телепатия', 'Чтение мыслей', 'Телепатическое обнаружение', 'Суггестия (псионические атаки)', 'Контроль сознания', 'Создание иллюзий', 'Манипуляция памятью', 'Генерация псионической материи * Астральная проекция', 'Перенос разума', 'Эйдетическая память', 'Выдающийся лидер, тактик и стратег', 'Обширные знания в генетике'],
                   'Iron Man': ['Гениальный интеллект', 'Обширные знания во многих технических науках', 'Широкий доступ к сверхсовременным технологиям', 'Выдающийся изобретатель и инженер', 'Киберпатическая связь с бронекостюмом', 'Обширные познания в боевых искусствах', 'Телепатическая связь со всемирной паутиной'],
                   'Wonder Woman': ['Сверхчеловеческая сила, скорость, выносливость, ловкость и стойкость', 'Мастер боевых искусств', 'Ограниченная неуязвимость', 'Бессмертие', 'Исцеляющий фактор', 'Полёт', 'Понимание животных'],
                   'Mister Fantastic': ['высокий и гениальный интеллект', 'широкие знания в различных областях науки', 'некоторая устойчивость к повреждениям', 'способность растягивать и деформировать своё тело'],
                   'Deadpool': ['Выдающееся владение холодным оружием', 'Мастер рукопашного боя', 'Проворство и ловкость', 'Опытный тактик и стратег', 'Превосходные акробатические данные', 'Высокий болевой порог', 'Регенерация и бессмертие', 'Сверхчеловеческая иммунная система', 'Невосприимчивость к телепатии', 'Физические данные на пике человеческого потенциала', 'Абсолютная непредсказуемость', 'Экстрасенсорика', 'Шестое чувство'],
                   'Aquaman': ['Адаптация Амфибии', 'Эхолокация', 'Регенерация', 'Сверхчеловеческие характеристики', 'Способность телепатически управлять рыбами, земноводными и млекопитающими', 'Устойчивость к энергетическим атакам', 'Понимание водных существ'],
                   'Dr. Stephen Vincent Strange': ['Высокие познания в магии', 'Глубокие оккультные и мистические знания', 'Высокий уровень интеллекта', 'Создание клонов', 'Неуязвимость', 'Астральная и ментальная проекция', 'Гипноз', 'Телепортация', 'Иллюзии', 'Регенерация', 'Неосязаемость и невидимость', 'Трансформация материи', 'Манипуляции временем', 'Превосходное владение навыками ближнего боя', 'Фотографическая память', 'Глубокие познания в области психологии и медицины']}
herous_gadgets = {'Superman': [],
                  'Batman': ['бэткрюк', 'тросомёт', 'бэтаранг', 'аптечка', 'дымовые шашки'],
                  'Thor': ['Молот Мьёльнир', 'Громсекира', 'Пояс Мегингёрд'],
                  'Hulk': [],
                  'Captain America': ['Щит из вибраниума', 'Шлем из вибраниума'],
                  'Spider-Man': ['Веб-шутеры', 'Паучьи жучки','Различные костюмы с индивидуальными свойствами', 'пояс со встроенным фонариком', 'пауко-боты (глаза и уши Человека-паука следят и наблюдают круглосуточно за Нью-Йорком. Размер роботов-пауков — 5 см)', 'глайдер (глайдер появлялся всего один раз в комиксах)', 'Питер Паркер со своей организацией разработал мини-компьютер размером с простой смартфон и гигантскими йохабайтами памяти и выходом в интернет в любом месте в любое время'],
                  'Wolverine': ['Адамантиевый скелет и когти', 'Костюм Людей Икс', 'Различные кинжалы, мечи, катаны и огнестрельное оружие'],
                  'Green Lantern': ['Кольцо Силы', 'Батарея Силы для зарядки кольца'],
                  'Flash': ['Особый костюм, способный выдерживать высокие скорости'],
                  'Professor X': ['Компьютер Церебро', 'Левитирующее инвалидное кресло'],
                  'Iron Man': ['Портативный ядерный реактор в груди, поддерживающий жизнь и являющийся источником энергии для брони. Серия экзоскелетов, дающих: сверхзвуковой полёт; высокую стойкость к повреждениям; использование репульсорных лучей на руках и многочисленного оружия, вмонтированного в костюм;использование унилуча на груди'],
                  'Wonder Woman': ['Лассо Истины', 'Защитные браслеты', 'Магический меч', 'Щит'],
                  'Mister Fantastic': ['костюм из нестабильных молекул, способный неограниченно растягиваться'],
                  'Deadpool': ['Различное холодное и огнестрельное оружие', 'Высокотехнологичные гаджеты и устройства'],
                  'Aquaman': ['Пентозубец'],
                  'Dr. Stephen Vincent Strange': ['Плащ Левитации, позволяющий летать и менять структуру', 'Книга Вишанти', 'Книга Калиостро', 'Амулет власти', 'Кольца стихий', 'Магический дробовик', 'Жезл Ватуумба', 'Свиток Ватуумба', 'Око Агамотто', 'Сфера Агамотто']}
supers_abilitys = ['Кидать живые бананы', 'Нюхать клей', 'Ходить в школу', 'Бензин']
round_pre = ['Финале', '1/2 Финала', '1/4 Финала', '1/8 Финалa', '1/16 Финалa', '1/32 Финалa', '1/64 Финалa', '1/128 Финалa', '1/256 Финалa', '1/512 Финалa', '1/1024 Финалa']

balance = 1000
list_coef, list_bet = [2, 4, 10], [100, 1000, 10000]
list_try2, list_try4, list_try10 = [6, 9, 13], [5, 8, 12], [4, 7, 11]

# мейн программа
def supers(kolvo_hero, who_makes=1):
    if who_makes == 1:
        for i in range(1, kolvo_hero - int(len(herous_powers)) + 1):
            super = f'Супер №{i}'
            power = f'{rr(1, 100)}'
            herous_powers.setdefault(super, power)
            herous_abilitys.setdefault(super, ch(supers_abilitys))
    else:
        print('Приветствую на фабрике суперов')
        print('Твердыня будет очень зол на меня, да и пошел он нахуй!')
        print(f'Короче, босс сказал надо сделать {kolvo_hero-int(len(herous_powers))} суперов')
        print('Пиши сюда имя нового уебана и его силу')
        create_ability = []
        for i in range(1, kolvo_hero - int(len(herous_powers)) + 1):
            name_power = input().split()
            if len(name_power) > 1:
                super = name_power[0]
                power = int(name_power[1])
                herous_powers.setdefault(super, power)
                print('Класс, новый уебан готов, осталось придумать ему способность(Напишите 1), но можем оставить и так, у него само что-то да отрастет(Напишите 2)')
                answer_ability = int(input())
                while answer_ability == 1 and answer_ability == 2:
                    print('Напишите число')
                    answer_kolvo_hero_group = int(input())
                if answer_ability == 2:
                    herous_abilitys.setdefault(super, ch(supers_abilitys))
                else:
                    print('Ну давай, придумай что-нибудь ебанутое')
                    ability1 = input()
                    create_ability.append(ability1)
                    herous_abilitys.setdefault(super, ability1)
                print(f'{i} супер готов')
                print('Пиши имя и силу для новой твари или если заебала работа на этом блядском заводе, напиши 3, эта хуйня сама все доделает')
            else:
                print('Молодец, правильный выбор')
                break
        for i in range(1, abs(int(len(herous_powers)) - kolvo_hero) + 1):
            super = f'Супер №{i}'
            power = f'{rr(1, 100)}'
            herous_powers.setdefault(super, power)
            herous_abilitys.setdefault(super, ch(supers_abilitys))
        return create_ability
def gr(kolvo_rounds):
    for i in range(1, 11):
        if 2**i == kolvo_rounds:
            grands = i
            break
    return grands
def rou(grands):
    #for_round = []
    #for i in range(grands, 0, -1):
     #   for_round.append(2**i)
    round = []
    for i in range(grands):
        round.append(round_pre[i])
    return round
def reshafl(ltourhero, kolvo_hero, who_change=2):
    new_herous = []
    if who_change == 2:
        sh(ltourhero)
        for i in range(kolvo_hero):
            new_herous.append(ltourhero[i])
    else:
        print('Напишите имена всех героев, которых вы выбрали на одной строке через запятую')
        for i in input().split(', '):
            new_herous.append(i)
    return new_herous
def live_herous(ltourhero, for_live_herous):
    l1, l2 = ltourhero, for_live_herous
    l3 = []
    for i in l1:
        if i not in l2:
            l3.append(i)
    for i in l3:
        print(i, herous_powers[i])
def group_stage(kolvo_hero, answer_kolvo_hero_group=4, input_hero_from_group=2, matches_in_group='да', answer_make_group='нет'):
    lhero, lpower, lability = [], [], []
    lhero2, lpower2, lability2 = [], [], []
    for hero, power in herous_powers.items():
        lhero.append(hero)
    groups = [[] * int(kolvo_hero / answer_kolvo_hero_group) for _ in range(int(kolvo_hero / answer_kolvo_hero_group))]
    sh(lhero)
    x = 0
    name_groups = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                   'U', 'V', 'W', 'X', 'Y', 'Z']
    q = 0
    if answer_make_group.lower() == 'нет':
        for i in range(int(kolvo_hero / answer_kolvo_hero_group)):
            for j in range(answer_kolvo_hero_group):
                groups[i].append(lhero[x])
                x += 1
    else:
        print('Герои и их суммарная сила допступная для выбора')
        for k, v in herous_powers.items():
            print(k, v)
        ln = 0
        useless_hero = []
        for i in range(int(kolvo_hero / answer_kolvo_hero_group)):
            if i >= 1:
                print('Хотите посмотреть список героев, которых вы еще не выбрали?')
                lives_hero = input()
                if lives_hero.lower() == 'да':
                    live_herous(groups[i], herous_powers)
            print(f'Напишите на одной строке через запятую каких героев вы хотите добавить в группу {name_groups[q]}')
            name_hero = input().split(', ')
            for k in name_hero:
                groups[i].append(k)
                useless_hero.append(k)
            print('Прекрасный выбор!')
            q += 1
            ln += 1
            print('Если хотите, чтобы дальше группы создал рнадом, напишите 3')
            answer_random = int(input())
            if answer_random == 3:
                break
        if answer_random == 3:
            gr = []
            for i in range(kolvo_hero):
                if lhero[x] not in useless_hero:
                    gr.append(lhero[x])
                x += 1
            x = 0
            for i in range(int(kolvo_hero / answer_kolvo_hero_group) - (int(kolvo_hero / answer_kolvo_hero_group) - ln), int(kolvo_hero / answer_kolvo_hero_group)):
                for j in range(answer_kolvo_hero_group):
                    groups[i].append(gr[x])
                    x += 1
    winers_up = dict()
    q = 0
    for i in range(len(groups)):
        now = dict()
        winers_down = []
        for k in range(answer_kolvo_hero_group):
            now.setdefault(groups[i][k], 0)
        names_hero = []
        for k, v in now.items():
            names_hero.append(k)
        print(f'Группа {name_groups[q]}:')
        for m in groups[q]:
            print(m, end=' ')
        print()
        for j in range(len(groups[i])):
            for l in range(answer_kolvo_hero_group):
                if l != j:
                    hero1, hero2 = groups[i][j], groups[i][l]
                    llhero, llpower, llability = [hero1, hero2], [herous_powers[hero1], herous_powers[hero2]], [herous_abilitys[hero1], herous_abilitys[hero2]]
                    #print(llhero, llpower)
                    game(llhero, llpower)
                    r1, r2 = rr(int(llpower[0])), rr(int(llpower[1]))
                    if r1 > r2:
                        if matches_in_group.lower() == 'да':
                            print(f'{llhero[0]} победил {llhero[1]}, благодаря способности {ch(llability[0])}')
                            print()
                        now[hero1] += 3
                    elif r1 == r2:
                        if matches_in_group.lower() == 'да':
                            print(f'Ничья у {llhero[0]} и {llhero[1]}')
                            print()
                        now[hero1] += 1
                        now[hero2] += 1
                    else:
                        if matches_in_group.lower() == 'да':
                            print(f'{llhero[1]} победил {llhero[0]}, благодаря способности {ch(llability[1])}')
                            print()
                        now[hero2] += 3
        if matches_in_group.lower() == 'да':
            print(f'Группа {name_groups[q]} сыграла все свои матчи!')
        print()
        ochki, names = [], []
        for k, v in now.items():
            print(f'{k} всего набрал {v} очков')
            ochki.append(v)
            names.append(k)
        input_hero = 0
        max1 = max(now.values())
        free_place = input_hero_from_group
        for i in range(input_hero_from_group):
            proverka = 0
            maxv = max(now.values())
            #print(maxv, winers_down, now)
            for k, v in now.items():
                if v == maxv and i == 0 and ochki.count(v) < 3 and input_hero != input_hero_from_group:
                    znak = k
                    input_hero += 1
                    free_place -= 1
                    break
                if v == max1 and ochki.count(v) == 2 and input_hero != input_hero_from_group and i != 0:
                    znak = k
                    input_hero += 1
                    free_place -= 1
                    break
                if v == maxv and ochki.count(v) == 1 and input_hero != input_hero_from_group:
                    znak = k
                    input_hero += 1
                    free_place -= 1
                    break
                if v == max1 and ochki.count(v) != 2:
                    znak = k
                    input_hero += 1
                    free_place -= 1
                    break
                if v == maxv and ochki.count(v) == 2 and input_hero + 2 <= input_hero_from_group:
                    dlt = []
                    for t, h in now.items():
                        if h == v:
                            winers_down.append(t)
                            free_place -= 1
                            input_hero += 1
                            dlt.append(t)
                    for i in range(len(dlt)):
                        del now[dlt[i]]
                    proverka = 1
                    break
                if v == maxv and ochki.count(v) == 3 and input_hero + 3 <= input_hero_from_group:
                    dlt = []
                    for t, h in now.items():
                        if h == v:
                            winers_down.append(t)
                            free_place -= 1
                            input_hero += 1
                            dlt.append(t)
                    for i in range(len(dlt)):
                        del now[dlt[i]]
                    proverka = 1
                    break
                if ochki.count(v) == 2 and i != 0 and maxv == v and input_hero != input_hero_from_group:
                    for l, h in now.items():
                        if h == v and l != k:
                            znak = l
                    print(f'У {k} и {znak} одинаковое количество очков')
                    print(
                        f'Вы можете выбрать кто выйдет из группы(Напишите 1) или устроить поединок между ними(Напишите 2)')
                    answer_row = int(input())
                    while type(answer_row) != int:
                        print('Чукча, число введи, але')
                        answer_row = int(input())
                    if answer_row == 1:
                        print('Напишите кто должен пройти дальше')
                        znak = input()
                    else:
                        rr1, rr2 = rr(maxv), rr(v)
                        if rr1 > rr2:
                            print(f'{znak} победил {k}')
                        else:
                            print(f'{k} победил {znak}')
                            znak = k
                    input_hero += 1
                    free_place -= 1
                    break
                if ochki.count(v) >= 3 and input_hero + 2 >= input_hero_from_group and maxv == v and free_place != 0:
                    print(f'Ух ты! у {ochki.count(v)} героев одинаковое количество очков')
                    print(f'Вам надо выбрать {input_hero_from_group-input_hero} героя, которые выйдут из группы')
                    print('Список героев:')
                    for j, h in now.items():
                        if h == v:
                            print(j, end=' ')
                    print()
                    if input_hero_from_group-input_hero >= 2:
                        print('Напишите кто должен пройти дальше на одной строке через запятую')
                    else:
                        print('Напишите кто должен пройти дальше')
                    znak = input().split(', ')
                    for t in znak:
                        winers_down.append(t)
                        free_place -= 1
                        input_hero += 1
                        del now[t]
                    proverka = 1
                    break
            print(winers_down, maxv, znak, input_hero, free_place)
            if proverka == 0 and input_hero <= input_hero_from_group:
                winers_down.append(znak)
                del now[znak]
                if input_hero == input_hero_from_group:
                    input_hero += 10
            #print(winers_down, maxv, znak)
            if free_place == 0:
                break
        winers_up.setdefault(name_groups[q], winers_down)
        q += 1
        if int(kolvo_hero / answer_kolvo_hero_group) == len(winers_up):
            print()
        else:
            for i in range(3):
                print()
        #print(winers_up)
    winers = ['*' for i in range(int(kolvo_hero / input_hero_from_group) * 2)]
    #print(winers_up)
    l1, l2 = [], []
    q1, q2 = 0, 0
    for i in range(0, len(winers_up), 2):
        for k1 in winers_up[name_groups[i]]:
            l1.append(k1)
        for k2 in list(reversed(winers_up[name_groups[i+1]])):
            l2.append(k2)
    for j in range(0, len(l1)*2, 2):
        winers[j] = l1[q1]
        q1 += 1
    for j2 in range(1, len(l2)*2, 2):
        winers[j2] = l2[q2]
        q2 += 1
    print('Групповой этап закончился')
    print()
    return winers

# казино
def is_bet_good(bet):
    return len(bet) == 2 and 50 <= int(bet[0]) <= balance and bet[1] in herous_powers
def game(llhero, llpower, p=0):
    global balance
    who1, who2 = llhero[0], llhero[1]
    reit1, reit2 = rr(int(llpower[0])), rr(int(llpower[1]))
    draw = abs(100 - reit1 - reit2)
    print('Итак, ситуация такова:')
    print('\nТвой баланс:', balance, 'монет')
    print('Доступные коэффициенты:')
    print(f'{100/reit1} на победу {llhero[0]}')
    print(f'{draw} на ничью между {llhero[0]} и {llhero[1]}')
    print(f'{100/reit2} на победу {llhero[1]}')
    print('Чтобы сделать ставку, введите через запятую: [Cумма ставки (мин. 50 окусов)] [Имя героя] (к примеру: 500, Wolverine)')

    bet = input().split(', ')
    while not is_bet_good(bet):
        bet = [int(i) for i in input('Неправильный формат! Формат должен быть: [Cумма ставки (мин. 100 окусов)] [Имя героя] (к примеру: 500, Wolverine)').split()]
    if p == 1:
        if (reit1 > reit2 and bet[1] == who1) or (reit2 > reit1 and bet[1] == who2) or (reit1 == reit2 and bet[1] == draw):
            print('Вы выиграли')
        elif (reit1 > reit2 and bet[1] == who2) or (reit2 > reit1 and bet[1] == who1) or (reit1 != reit2 and bet[1] == draw):
            print('Вы проиграли')


    return reit1, reit2


def tournament():
    t = 1
    x = 0
    ltourhero, ltourhero2 = [], []
    print('Сколько участников должно быть?(число должно быть 2**x)')
    kolvo_hero = int(input())
    while kolvo_hero % 2 != 0:
        print('Число не соответсвует условию, напишите новое число')
        kolvo_hero = int(input())
    if kolvo_hero > len(herous_powers):
        print('Вы выбрали больше героев, чем есть в базе данных, в таком случае запускается фабрика суперов')
        print('На этой фабрике создаются искуственно выращенные герои, может вы хотите дать некоторым(или всем) им имена, общую силу и уникальную способность')
        answer_supers = input()
        while answer_supers.lower() != 'да' and answer_supers.lower() != 'нет':
            print('Извините, но я слишком тупая программа, я могу понимать ответы только "да" и "нет"')
            answer_supers = input()
        if answer_supers.lower() == 'нет':
            supers(kolvo_hero)
        else:
            create_abilitys = supers(kolvo_hero, who_makes=2)
        print('Вы выбрали много героев, может включить групповой этап?')
        answer_group = input()
        while answer_group.lower() != 'да' and answer_group.lower() != 'нет':
            print('Извините, но я слишком тупая программа, я могу понимать ответы только "да" и "нет"')
            answer_group = input()
        if answer_group.lower() == 'да':
            print('Сколько героев должно быть в одной группе?')
            answer_kolvo_hero_group = int(input())
            while answer_kolvo_hero_group % 2 != 0 or answer_kolvo_hero_group < 4:
                print('Число не соответсвует условию, напишите новое число')
                print('Минимальное число героев в группе 4, введите количество героев в группе еще раз')
                answer_kolvo_hero_group = int(input())
            while kolvo_hero % answer_kolvo_hero_group != 0:
                print('Общее количество героев не подходит для того, чтобы поделить их на равные части')
                print('Надо или изменить общее количество героев(Напишите 1) или изменить количество героев в группе(Напишите 2)')
                answer1 = int(input())
                if answer1 == 1:
                    kolvo_hero = int(input())
                else:
                    answer_kolvo_hero_group = int(input())
            print('Сколько героев должно выходить из группы?')
            input_hero_from_group = int(input())
            while input_hero_from_group % 2 != 0 and input_hero_from_group != 1:
                if input_hero_from_group == 0:
                    print('Минимальное число героев, которое выходит из группы 1, напишите новое число')
                else:
                    print('Общее число игроков, вышедших из всех групп, должно делиться на 2 нацело, напишите новое число')
                input_hero_from_group = int(input())
            answer_make_group = input()
            while answer_make_group.lower() != 'да' and answer_make_group.lower() != 'нет':
                print('Извините, но я слишком тупая программа, я могу понимать ответы только "да" и "нет"')
                answer_make_group = input()
            print('Выводить матчи в группе?')
            matches_in_group = input()
            while matches_in_group.lower() != 'да' and matches_in_group.lower() != 'нет':
                print('Извините, но я слишком тупая программа, я могу понимать ответы только "да" и "нет"')
                matches_in_group = input()
            gp = group_stage(kolvo_hero, answer_kolvo_hero_group, input_hero_from_group, matches_in_group, answer_make_group)
            for hero, power in herous_powers.items():
                if hero in gp:
                    ltourhero.append(hero)
            kolvo_t_rounds = len(ltourhero)
        if answer_group.lower() == 'нет':
            for hero, power in herous_powers.items():
                ltourhero.append(hero)
            kolvo_t_rounds = len(ltourhero)
    else:
        for hero, power in herous_powers.items():
            ltourhero.append(hero)
        kolvo_t_rounds = len(ltourhero)
        create_abilitys = []
    if len(herous_powers) > kolvo_hero:
        print('Хотите сами выбрать героев для турнира?')
        answer_reschafl = input()
        if answer_reschafl.lower() == 'да':
            ltourhero = reshafl(ltourhero, kolvo_hero, who_change=1)
            kolvo_t_rounds = len(ltourhero)
        else:
            ltourhero = reshafl(ltourhero, kolvo_hero)
            kolvo_t_rounds = len(ltourhero)
    print('Герои и их суммарная сила доступные для выбора')
    if len(herous_powers) > kolvo_hero:
        for k, v in herous_powers.items():
            if k in ltourhero:
                print(k, v)
    else:
        for k, v in herous_powers.items():
            if k in ltourhero:
                print(k, v)
    for_round = rou(gr(kolvo_t_rounds))
    for i in range(gr(kolvo_hero)):
        if len(ltourhero2) == 0 and abs(x) != len(for_round):
            x -= 1
            for_live_herous = []
            for i in range(0, len(ltourhero), 2):
                if for_round[x] != 'Финале':
                    print(f'Сейчас вы выберите {t} пару в {for_round[x]}')
                    if t > 1:
                        print('Хотите посмотреть список героев, которые еще не учавствовали в нанешнем раунде?')
                        lives_hero = input()
                        if lives_hero.lower() == 'да':
                            live_herous(ltourhero, for_live_herous)
                else:
                    print('Финал!!!')
                print('Выберите двоих и напишите их имена, каждое на отдельной строке', end='\n')
                t += 1
                hero1 = input()
                hero2 = input()
                llhero, llpower, llability = [hero1, hero2], [herous_powers[hero1], herous_powers[hero2]], [herous_abilitys[hero1], herous_abilitys[hero2]]
                #print(llhero, llpower)
                game(llhero, llpower)
                if rr(int(llpower[0])) > rr(int(llpower[1])):
                    print(f'В {for_round[x]} {hero1} победил {hero2}, благодаря способности {ch(llability[0]) if "Супер" not in llhero[0][:5] and llability[0] not in create_abilitys else llability[0]}')
                    print()
                    ltourhero2.append(hero1)
                    for_live_herous.append(hero1)
                    for_live_herous.append(hero2)
                else:
                    print(f'В {for_round[x]} {hero2} победил {hero1}, благодаря способности {ch(llability[1]) if "Супер" not in llhero[1][:5] and llability[1] not in create_abilitys else llability[1]}')
                    print()
                    ltourhero2.append(hero2)
                    for_live_herous.append(hero1)
                    for_live_herous.append(hero2)
            lhero.clear()
            t = 1
            for_live_herous = []

        elif len(lhero) == 0 and abs(x) != len(for_round):
            x -= 1
            for i in range(0, len(ltourhero2), 2):
                if for_round[x] != 'Финале':
                    print(f'Сейчас вы выберите {t} пару в {for_round[x]}')
                    if t > 1:
                        print('Хотите посмотреть список героев, которые еще не учавствовали в нанешнем раунде?')
                        lives_hero = input()
                        if lives_hero.lower() == 'да':
                            live_herous(ltourhero2, for_live_herous)
                else:
                    print('Финал!!!')
                print('Выберите двоих и напишите их имена, каждое на отдельной строке', end='\n')
                t += 1
                hero1 = input()
                hero2 = input()
                llhero, llpower, llability = [hero1, hero2], [herous_powers[hero1], herous_powers[hero2]], [herous_abilitys[hero1], herous_abilitys[hero2]]
                #print(llhero, llpower)
                game(llhero, llpower)
                if rr(int(llpower[0])) > rr(int(llpower[1])):
                    print(f'В {for_round[x]} {hero1} победил {hero2}, благодаря способности {ch(llability[0]) if "Супер" not in llhero[0][:5] and llability[0] not in create_abilitys else llability[0]}')
                    print()
                    ltourhero.append(hero1)
                    for_live_herous.append(hero1)
                    for_live_herous.append(hero2)
                else:
                    print(f'В {for_round[x]} {hero2} победил {hero1}, благодаря способности {ch(llability[1]) if "Супер" not in llhero[1][:5] and llability[1] not in create_abilitys else llability[1]}')
                    print()
                    ltourhero.append(hero2)
                    for_live_herous.append(hero1)
                    for_live_herous.append(hero2)
            lhero2.clear()
def random():
    x = 0
    lhero, lpower, lability = [], [], []
    lhero2, lpower2, lability2 = [], [], []
    print('Сколько участников должно быть?(число должно быть 2**x)')
    kolvo_hero = 32 #int(input())
    while kolvo_hero % 2 != 0:
        print('Число не соответсвует условию, напишите новое число')
        kolvo_hero = int(input())
    if kolvo_hero > len(herous_powers):
        print('Вы выбрали больше героев, чем есть в базе данных, в таком случае запускается фабрика суперов')
        print('На этой фабрике создаются искуственно выращенные герои, может вы хотите дать некоторым(или всем) им имена, общую силу и уникальную способность')
        print('Хотите в этом поучаствовать?')
        answer_supers = 'нет' #input()
        while answer_supers.lower() != 'да' and answer_supers.lower() != 'нет' and answer_supers.lower() != 'хочу' and answer_supers.lower() != 'не хочу':
            print('Извините, но я слишком тупая программа, я могу понимать ответы только "да" и "нет", "хочу", "не хочу"')
            answer_supers = input()
        if answer_supers.lower() == 'нет':
            supers(kolvo_hero)
            create_abilitys = []
        else:
            create_abilitys = supers(kolvo_hero, who_makes=2)
        print('Вы выбрали много героев, может включить групповой этап?')
        answer_group = 'нет' #input()
        while answer_group.lower() != 'да' and answer_group.lower() != 'нет':
            print('Извините, но я слишком тупая программа, я могу понимать ответы только "да" и "нет"')
            answer_group = input()
        if answer_group.lower() == 'да':
            print('Сколько героев должно быть в одной группе?')
            answer_kolvo_hero_group = int(input())
            while answer_kolvo_hero_group % 2 != 0 or answer_kolvo_hero_group < 4:
                print('Число не соответсвует условию, напишите новое число')
                print('Минимальное число героев в группе 4, введите количество героев в группе еще раз')
                answer_kolvo_hero_group = int(input())
            while kolvo_hero % answer_kolvo_hero_group != 0:
                print('Общее количество героев не подходит для того, чтобы поделить их на равные части')
                print('Надо или изменить общее количество героев(Напишите 1) или изменить количество героев в группе(Напишите 2)')
                answer1 = int(input())
                if answer1 == 1:
                    kolvo_hero = int(input())
                else:
                    answer_kolvo_hero_group = int(input())
            print('Сколько героев должно выходить из группы?')
            input_hero_from_group = int(input())
            while input_hero_from_group % 2 != 0 and input_hero_from_group != 1:
                if input_hero_from_group == 0:
                    print('Минимальное число героев, которое выходит из группы 1, напишите новое число')
                else:
                    print('Общее число игроков, вышедших из всех групп, должно делиться на 2 нацело, напишите новое число')
                input_hero_from_group = int(input())
            print('Хотите сами составлять группы?')
            answer_make_group = input()
            while answer_make_group.lower() != 'да' and answer_make_group.lower() != 'нет':
                print('Извините, но я слишком тупая программа, я могу понимать ответы только "да" и "нет"')
                answer_make_group = input()
            print('Выводить матчи в группе?')
            matches_in_group = input()
            while matches_in_group.lower() != 'да' and matches_in_group.lower() != 'нет':
                print('Извините, но я слишком тупая программа, я могу понимать ответы только "да" и "нет"')
                matches_in_group = input()
            gp = group_stage(kolvo_hero, answer_kolvo_hero_group, input_hero_from_group, matches_in_group, answer_make_group)
            for hero, power in herous_powers.items():
                if hero in gp:
                    lhero.append(hero)
            kolvo_rounds = len(lhero)
        if answer_group.lower() == 'нет':
            for hero, power in herous_powers.items():
                lhero.append(hero)
            kolvo_rounds = len(lhero)
            sh(lhero)
    else:
        for hero, power in herous_powers.items():
            lhero.append(hero)
        kolvo_rounds = len(lhero)
        sh(lhero)
        create_abilitys = []
    if len(herous_powers) > kolvo_hero:
        print('Хотите сами выбрать героев для турнира?')
        answer_reschafl = input()
        if answer_reschafl.lower() == 'да':
            lhero = reshafl(lhero, kolvo_hero, who_change=1)
            kolvo_rounds = len(lhero)
        else:
            lhero = reshafl(lhero, kolvo_hero)
            kolvo_rounds = len(lhero)
    for_round = rou(gr(kolvo_rounds))
    mark1, mark2, tm1, tm2 = 0, 0, 0, 0
    for j in range(gr(kolvo_hero)):
        if len(lhero2) == 0 and abs(x) != len(for_round):
            x -= 1
            if for_round[x] != 'Финале':
                print(f'Пары в {for_round[x]}:')
            else:
                print('Финал:')
            for i in range(0, len(lhero), 2):
                print(f'{lhero[i]} - {lhero[i + 1]}')
            print()
            for i in range(0, len(lhero), 2):
                llhero, llpower, llability = [lhero[i], lhero[i + 1]], [herous_powers[lhero[i]], herous_powers[lhero[i + 1]]], [herous_abilitys[lhero[i]], herous_abilitys[lhero[i + 1]]]
                if answer3 == 'да':
                    game(llhero, llpower)
                if (rr(int(llpower[0])) > rr(int(llpower[1])) and answer3 != 'нет') or (reit1 > reit2 and answer3 != 'да'):
                    print(f'В {for_round[x]} {llhero[0]} победил {llhero[1]}, благодаря способности {ch(llability[0]) if "Супер" not in llhero[0][:5] and llability[0] not in create_abilitys else llability[0]}')
                    print()
                    lhero2.append(llhero[0])
                    lpower2.append(llpower[0])
                    lability2.append(llability[0])
                else:
                    print(f'В {for_round[x]} {llhero[1]} победил {llhero[0]}, благодаря способности {ch(llability[1]) if "Супер" not in llhero[1][:5] and llability[1] not in create_abilitys else llability[1]}')
                    print()
                    lhero2.append(llhero[1])
                    lpower2.append(llpower[1])
                    lability2.append(llability[1])
            game([], [], p=1)
            lhero.clear()
        elif len(lhero) == 0 and abs(x) != len(for_round):
            x -= 1
            if for_round[x] != 'Финале':
                print(f'Пары в {for_round[x]}:')
            else:
                print('Финал:')
            for i in range(0, len(lhero2), 2):
                print(f'{lhero2[i]} - {lhero2[i + 1]}')
            print()
            for i in range(0, len(lhero2), 2):
                llhero, llpower, llability = [lhero2[i], lhero2[i + 1]], [herous_powers[lhero2[i]], herous_powers[lhero2[i + 1]]], [herous_abilitys[lhero2[i]], herous_abilitys[lhero2[i + 1]]]
                #print(llhero, llpower)
                if answer3 == 'да':
                    game(llhero, llpower)
                if (rr(int(llpower[0])) > rr(int(llpower[1])) and answer3 != 'нет') or (reit1 > reit2 and answer3 != 'да'):
                    print(f'В {for_round[x]} {llhero[0]} победил {llhero[1]}, благодаря способности {ch(llability[0]) if "Супер" not in llhero[0][:5] and llability[0] not in create_abilitys else llability[0]}')
                    print()
                    lhero.append(llhero[0])
                    lpower.append(llpower[0])
                    lability.append(llability[0])
                else:
                    print(f'В {for_round[x]} {llhero[1]} победил {llhero[0]}, благодаря способности {ch(llability[1]) if "Супер" not in llhero[1][:5] and llability[1] not in create_abilitys else llability[1]}')
                    print()
                    lhero.append(llhero[1])
                    lpower.append(llpower[1])
                    lability.append(llability[1])


            lhero2.clear()
def for_fun():
    battle_answer = 'да'
    print('Сколько участников должно быть?(число должно быть 2**x)')
    kolvo_hero = int(input())
    if kolvo_hero > len(herous_powers):
        supers(kolvo_hero)
    print('Герои и их суммарная сила доступные для выбора')
    for k, v in herous_powers.items():
        print(k, v)
    while battle_answer.lower() == 'да':
        print('Выберите двоих и напишите их имена, каждое на отдельной строке', end='\n')
        hero1 = input()
        hero2 = input()
        if rr(int(herous_powers[hero1])) > rr(int(herous_powers[hero2])):
            print(f'{hero1} победил {hero2}, благодаря способности {ch(herous_abilitys[hero1])}')
        else:
            print(f'{hero2} победил {hero1}, благодаря способности {ch(herous_abilitys[hero2])}')
        print('Хотите Повторить?')
        battle_answer = input()
        if battle_answer.lower() == 'нет':
            break
        else:
            print('Надо вывести список героев еще раз?')
            if input().lower() == 'да':
                for k, v in herous_powers.items():
                    print(k, v)

x = 0
lhero, lpower, lability = [], [], []
lhero2, lpower2, lability2 = [], [], []

main_answer = 'да'
print('Здравствуйте! Это мини-игра про супергероев')

while main_answer.lower() == 'да':
    print('Прежде чем приступить к основной игре, есть один вопрос')
    print('Включить казино?')
    answer3 = input()
    while answer3.lower() != 'да' and answer3.lower() != 'нет':
        print('Извините, но я слишком тупая программа, я могу понимать ответы только "да" и "нет"')
        answer3 = input()
    if answer3 == 'да':
        print('Добро пожаловать в Казино. Меня зовут бот Владимир! Я помогу тебе освоиться в игре. Чтобы продолжить, введи "Далее"')
        print('\nИтак, правила игры просты. У тебя есть игровой баланс: 1000 монет. Ты можешь ставить их на исходы матчей. Ты готов начинать? Напиши "Да" или "Готов"')
        name = input('Сперва, тебе стоит представиться. Всё-таки нам предстоит провести вместе время, мне стоит знать, как тебя зовут :)\n')
        print('\n\nРад знакомству', name.title())

    print('Теперь можем приступить к соновной части!')
    print('Хотите ли вы выбирать пары для битв?')
    battle_answer = 'нет' #input()
    while battle_answer.lower() != 'да' and battle_answer.lower() != 'нет':
        print('Извините, но я слишком тупая программа, я могу понимать ответы только "да" и "нет"')
        battle_answer = input()
    if battle_answer.lower() == 'да':
        print('Хотите устроить свой турнир?')
        tournament_answer = input()
        while tournament_answer.lower() != 'да' and tournament_answer.lower() != 'нет':
            print('Извините, но я слишком тупая программа, я могу понимать ответы только "да" и "нет"')
            tournament_answer = input()
        if tournament_answer.lower() == 'да':
            tournament()
        else:
            for_fun()
    if battle_answer == 'нет':
        random()
    print('Хотите закончить(Напишите 1) или поменять режим(Напишите 2)')
    global_answer = int(input())
    if global_answer == 1:
        main_answer = 'нет'
    else:
        continue