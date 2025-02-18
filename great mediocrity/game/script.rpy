##### 추가한 부분
###함수 선언
init python:
    monologue_list = []                                                             #독백 저장 리스트
    is_monologue_active = False                                                     # 대사 꺼내기 가능 여부
    mono_active =False                                                              # 클릭 가로채기 가능 여부

    #대사집에 저장
    def mono_with_character(dialogue):
        monologue_list.append(dialogue)
    #대사 출력
    def handle_next_monologue():
        global is_monologue_active

        if len(monologue_list) > 1:
            is_monologue_active = True
            dialogue = monologue_list.pop(0)
            renpy.show_screen("monologue", dialogue=dialogue)
            renpy.restart_interaction()
        elif len(monologue_list) == 1:
            dialogue = monologue_list.pop(0)
            renpy.show_screen("monologue", dialogue=dialogue)
            is_monologue_active = False
        else: 
            renpy.hide_screen("monologue")
    #일반 대사 진행
    def handle_normal_dialogue():
        if not is_monologue_active:
            return True                                                                 # 일반 대사의 넘김이 가능한 경우에만 호출
        return False

    # 대화 중 독백
    def mono_with_image(dialogue, character, character_image):                           # 클릭 가로채기 방지
        renpy.show_screen("monologue_image_screen", char_img=character_image)            # 새로운 GUI 창에 캐릭터 이미지 표시 
        character(dialogue)
        renpy.hide_screen("monologue_image_screen")                                      # 기존 GUI에서 캐릭터 이름과 대사 출력
    # 대화 중 독백 사용하는 캐릭터 이미지에 사용(수정 중)
    #def mono_callback(who, what):
    #    global mono_active
    #    if mono_active and what is not None:
    #        renpy.hide_screen("monologue_image_screen")
    #        mono_active = False     

define mono = renpy.curry(renpy.call_screen)("monologue")
#####

##캐릭터 정의          
#1장 1절                       #김한중 주인공이므로 주황색, 나머지는 하얀색
define unknown = Character('???', color = "#ffffff")
define none = Character('', color = "#ffffff")
define han = Character('김한중', color = "#ffb700")
define boss = Character('동학군 두목', color = "#ffffff")
define burden = Character('동학군', color = "#ffffff")
#1장 2절                        #씬1 주인공 김한중, 씬2 주인공 어린 김원근만 주황색
define oweon = Character('어린 김원근', color = "#ffb700")
define oweon_two = Character('어린 김원근', color = "#ffffff")
define ms = Character('아낙네', color = "#ffffff")
define mother = Character('어머니', color = "#ffffff")
define doctor = Character("의원", color = "#ffffff")
define villa = Character("마을 사람", color = "#ffffff")
define young = Character("어린 김영근", color = "#ffffff")
define kook = Character("김국선", color = "#ffffff")
define stu_1 = Character("학생1", color = "#ffffff")
define stu_2 = Character("학생2", color = "#ffffff")
define tr = Character("상인", color = "#ffffff")

##배경
#1장 1절
image bg_burning_building = "images/background/chap1_1/burning_building.png"
image bg_yard = "images/background/chap1_1/yard.png"
image bg_burning = "images/background/chap1_1/burning.jpg"
#1장 2절
image bg_winter_mountain = "images/background/chap1_2/winter_mountain.png"
image bg_winter_mountain_night = "images/background/chap1_2/winter_mountain_night.png"
image bg_bedroom = "images/background/chap1_2/bedroom.png"
image bg_house_winter = "images/background/chap1_2/house_winter.png"
image bg_house = "images/background/chap1_2/house.png"
image bg_fpp = "images/background/chap1_2/first_person_perspective.png"
image bg_sky = "images/background/chap1_2/sky.png"
image bg_village = "images/background/chap1_2/village.png"
image bg_winter_road = "images/background/chap1_2/winter_road.png"
image bg_winter_road_afternoon = "images/background/chap1_2/winter_road_afternoon.png"
image bg_winter_road_night = "images/background/chap1_2/winter_road_night.png"
image bg_indoor = "images/background/chap1_2/indoor.png"
#1장 3절
image bg_sky_mountain = "images/background/chap1_2/sky_mountain.png"
image bg_tavern = "images/background/chap1_2/tavern.png"
image bg_kim_house = "images/background/chap1_2/kim_house.png"
image bg_school = "images/background/chap1_2/school.png"
image bg_market = "images/background/chap1_2/market.png"


##

##인물 이미지 원본
#1장 1절 원본
image han_image_bound = im.FactorScale("images/character/chap1_1/han_bound.png", 0.3, )
image han_image_loose =  im.FactorScale("images/character/chap1_1/han_loose.png", 0.3)
image boss_image = im.FactorScale("images/character/chap1_1/boss.png", 0.3)
image group_image = im.FactorScale("images/character/chap1_1/group.png", 0.3)
#1장 1절 불투명 적용
image boss_dark_image = im.MatrixColor(im.FactorScale("images/character/chap1_1/boss.png", 0.3), im.matrix.brightness(-0.3))
image han_image_bound_dark_image = im.MatrixColor(im.FactorScale("images/character/chap1_1/han_bound.png", 0.3), im.matrix.brightness(-0.3))
image han_image_loose_dark_image = im.MatrixColor(im.FactorScale("images/character/chap1_1/han_loose.png", 0.3), im.matrix.brightness(-0.3))
#1장 2절
image oweon_image = im.FactorScale("images/character/chap1_2/oweon.png", 0.3)
image dad_son_image = im.FactorScale("images/character/chap1_2/dad_son.png", 0.3)
image mother_image = im.FactorScale("images/character/chap1_2/mother.png", 0.3)
image tired_oweon_image = im.FactorScale("images/character/chap1_2/tired_oweon.png", 0.3)
image smile_oweon_image = im.FactorScale("images/character/chap1_2/SmileImage.png", 0.3)
image sulk_oweon_image = im.FactorScale("images/character/chap1_2/SulkImage.png", 0.3)
image kim_standing_image = im.FactorScale("images/character/chap1_2/KimStanding.png",0.3)
image kim_smile_image = im.FactorScale("images/character/chap1_2/KimSmile.png",0.3)
image doctor_image = im.FactorScale("images/character/chap1_2/Doctor.png",0.3)
image doctor_edit_image = im.FactorScale("images/character/chap1_2/Doctor_edit.png",0.3)
image young_image = im.FactorScale("images/character/chap1_2/young.png",0.3)
image ms_image = im.FactorScale("images/character/chap1_2/villager.png",0.3)
#1장 3절
image Merchant_image = im.FactorScale("images/character/chap1_2/Merchant.png",0.3)
image cry_oweon_image = im.FactorScale("images/character/chap1_2/PreviousImage.png",0.3)
image student_image = im.FactorScale("images/character/chap1_2/Student.png",0.3)
image student_two_image = im.FactorScale("images/character/chap1_2/Studenttwo.png",0.3)

image 40_oweon = im.FactorScale("images/character/chap3_1/40_oweon.png", 0.8)

##

## 사용자 지정 페이드 인/아웃
define myfade_0 = Fade(0.5, 0.5, 0.0)   #0.5초간 페이드
define myfade_1 = Fade(1.0, 1.0, 0.0)    #1초간 페이드(씬 전환)
define myfade_2 = Fade(2.0, 2.0, 0.0)    #2초간 페이드(시간의 흐름)
define myfade_5 = Fade(5.0, 5.0, 0.0)    #5초간 페이드(절 전환)
init:
    transform myfade_character:    #등장인물 페이드 인
            alpha 0.0              # 처음엔 완전히 투명하게 시작
            linear 1.0 alpha 1.0

    #transform myfade_out_1:        #등장인물 페이드 아웃
    #        alpha 1.0              # 처음엔 완전히 보이는 상태에서 시작
    #        linear 1.0 alpha 0.0 

## 어두운 오버레이 이미지 정의
image dark_overlay = Solid("#000000")  # 50% 투명한 검은색

label start:
    scene black
    none "1894년"
    unknown "불이야!"
    unknown "불이야앗!!"

    play sound "audio/door_sound.mp3"

    scene bg_burning_building 
    unknown "네놈이 사장책이렸다! 순순히 이르는 대로 따라야지 반항하면 큰 코 다칠 줄 알아라!"
    play sound "audio/hit_sound.mp3"
    with myfade_1

    scene bg_yard 
    show han_image_bound_dark_image at myfade_character:
        xpos 200
        ypos 250
    show boss_image at myfade_character:
        xpos 900
        ypos 100
    boss "네가 이 곳의 사장책이냐"
    show boss_dark_image:
        xpos 900
        ypos 100
    show han_image_bound:
        xpos 200
        ypos 250
    han "......그렇다."
    hide boss_dark_image
    hide han_image_bound 
    boss "네가 왜 포박되었는지 아느냐?"
    show han_image_bound:
        xpos 200
        ypos 250
    show boss_dark_image:
        xpos 900
        ypos 100
    han "내가 묻고 싶은 말이다. 대체 어디서 온 누구냐? 뭣 때문에 소중한 나라의 곡식에 불을 지르고 이와 같이 소동을 피우는가!?"
    hide han_image_bound 
    hide boss_dark_image
    boss "네 말이 뜻 밖에도 시원하구나. 세상이 어찌 되었는지 들은바 없나?"
    show boss_dark_image:
        xpos 900
        ypos 100
    show han_image_bound:
        xpos 200
        ypos 250
    han "없다!"
    hide han_image_bound 
    hide boss_dark_image
    boss "어리석구나. 이곳 농민들한테 들으니 너는 우직하고 착해빠진 사창으로, 조정에서 하라는 대루만 하는 놈이라...."
    boss "이제 그 어리석음을 깨우쳐 주시 위해서 이야기해 줄기니 소상히 듣거라."
    boss "저기있는 곡식은 누가 먹을 거였나?"
    show han_image_bound:
        xpos 200
        ypos 250
    show boss_dark_image:
        xpos 900
        ypos 100
    han "내 알 배 아니다. 조정에 바칠 뿐이다."
    hide han_image_bound 
    hide boss_dark_image
    boss "나라를 생각하는 놈들이냐? 백성을 걱정하는 무리들이냐? 아니였제? "
    boss "제놈들 배창자 채우고 갖은 호강 다 하구, 주지육림에 몸을 담아 썩어 가는 줄 모르는  데 썼단 말이다!"
    boss "동학군은 일어섰다. 불의를 쳐부술 것이다. 너는 그 불의의 꼭두각시 노릇을 한 놈, 따라서 형을 받아야 마땅하다!"
    hide boss_image 
    hide han_image_bound_dark_image 
    with myfade_1

    scene black
    han "모두 옳은 소리다, 양반이 관직을 얻어 3년만 벼슬을 누리면 자손 대대로 만복을 누린다. 그만큼 양반은 백성들을 착취했고, 심지어는 죽기까지 했다."
    han "일찍 부모님을 여의고 간신히 간신히 살아오다가 이제 겨우 터를 잡아 끼니 굶지 않는 신세가 되었는제..... 이제 마지막인가. 이것이이 모든 것의 끝장인가."
    with fade
    scene bg_yard 
    show boss_image 
    boss "......"
    boss "김한중"
    hide boss_image
    show han_image_bound:
        xpos 550
        ypos 100
    han ".....?"
    hide han_image_bound
    show boss_image  
    boss "네가 김한중이라 하는 것은 틀림이 없겠제?"
    hide boss_image
    show han_image_bound:
        xpos 550
        ypos 100
    han "틀림없소"
    hide han_image_bound 
    show boss_image 
    boss "저자를 이리 끌어내리고 포승을 풀어라!"
    hide boss_image
    show group_image:
        xpos 550
        ypos 100
    burden "어째서 풀어줍니까?"
    hide group_image
    show boss_image
    boss "풀어주라 하잖나!"
    hide boss_image 
    with myfade_1

    scene bg_burning
    show boss_image 
    boss "일어나그라!" 
    boss "그대로 듣거라! 김한중은 우리가 동학군이라는 것을 아느냐?"
    hide boss_image 
    show han_image_loose at myfade_character:
        xpos 550
        ypos 100
    han "예."
    hide han_image_loose 
    show boss_image 
    boss "동학군은 불의를 꺾자고 하다가 너를 잡았다." 
    boss "그런데 근방 사람들 얘기를 들으니, 네 천성이 어질고 착실하여 비록 상부의 명령을 따르기는 했지만도, 네 멋대로 백성을 괴롭히지는 않았다는 것을 알았다."
    boss "목숨만은 부지하게 해줄테니 당장 이곳을 떠야 할 것이다."
    hide boss_image 
    show han_image_loose:
        xpos 550
        ypos 100
    han ".....!!"
    hide han_image_loose 
    show boss_image 
    boss "떠라! 오늘 밤 안으로 멀리멀리 떠라!"
    hide boss_image at myfade_character with dissolve
    with myfade_5
    jump chap1_2
    return

label chap1_2:
    scene black
    none "경주군 안강면 어느 산 속"
    scene bg_winter_mountain with myfade_1
    python:
        mono_with_character("날 죽이려던 무리들은 사라졌으나, 나를 반기지 않는 세상에 나갈 수 없었다.")
        mono_with_character("두꺼운 비위짱으로 나서려고 해도 언제 무슨 위험이 기다리고 있을지 모른다.")
        mono_with_character("나야 그렇다 치더라도 처자식이 문제다.")
        handle_next_monologue()
    none ""
    show oweon_image at myfade_character:
        xpos 550
        ypos 100
    oweon_two "아버지예" 
    hide oweon_image
    python:
        mono_with_character("산짐승이 득실거리는 산 속에 쪼그리다 해가 지면")
        mono_with_character("엉금엉금 기어나가 칡뿌리로 연명하는 이유")
        mono_with_character("이 아이가 내 마지막 꿈이다. 이 아이만 보면 서글프면서도 기쁨을 안겨준다")
        handle_next_monologue()
    none ""
    show oweon_image:
        xpos 550
        ypos 100
    oweon_two "매 맞은 데 다 났습니까?"
    hide oweon_image
    han "오냐, 원근아, 니는 걱정 말그래이"
    show oweon_image:
        xpos 550
        ypos 100
    oweon_two "와 맞았는교?"
    hide oweon_image
    han "그래 됐다 마"
    python:
        mono_with_character("이 아이가 무엇을 알겠는가? 탐관오리의 행패니, 동학의 뜻이니 말해도 알아들을 리 없다.")
        mono_with_character("그리고 행패 부리는 무리의 심부름하다 맞았다고 말하면 실망할지도 모른다.")
        handle_next_monologue()
    none ""
    han "그래 됐다. 원근아. 그 대신 니는 알아야 된대이. 사람이라 카는 것은 옳게 살아야 되는 기라. 욕심을 부려도 안 되고 남을 해쳐도 안되고, 게을러도 안되고, 거짓말 해도 안 되니라"
    han "원근이, 니는 커서 뭐가 될꼬?"
    show oweon_image:
        xpos 550
        ypos 100
    oweon_two "......"
    hide oweon_image
    han "니는 커서 가난한 사람 도와주고 불쌍한 사람 편들어 주는 사람 되면 참 좋겠다."
    han "영근아, 니도 들었나? 그래 사는 기다이"
    with dissolve
    scene bg_bedroom 
    show dad_son_image at myfade_character:
        xpos 550
        ypos 100
    han "절대로 남을 해치지 말그래이. 불쌍한 사람 도와주그래이."
    hide dad_son_image
    with myfade_2

    scene black
    python:
        mono_with_character("아버지가 왜 저렇게 산 속에 있어야만 하는지, 우리는 왜 아버지를 보러 몰래 다녀야만 하는지 알 수 없었다.")
        mono_with_character("어머니는 근방 일가 친처집에 다니는 게 일과이다.")
        mono_with_character("돌아올 때는 쌀이고 보리고 하다 못해 감자라도 얻어오셨다. 그리고 날이 밝기 전이면 어김없이 사람들 몰래 아버지에게 다녀오셨다.")
        mono_with_character("그러던 어느 날 산에 올라갔던 어머니는 한 걱정을 하며 돌아오셨다.")
        mono_with_character("그리고 해가 지자마자 또다시 집을 나서거더니 한밤 중이 되서야 끙끙 소리를 내며 아버지를 업고 들어오셨다.")
        mono_with_character("아버지의 병환이 심해졌다는 것을 단박에 알 수 있었다.")
        handle_next_monologue()
    none ""
    with dissolve

    scene bg_house_winter
    python:
        mono_with_character("아버지의 병환은 점점 심해져만 갔다.")
        mono_with_character("겨울이 되고나니 미음조차 끓일 것이 없어 어머니는 가슴만 쥐어뜯고 앉아 있었다.")
        handle_next_monologue()
    none ""
    with myfade_0

    scene bg_fpp 
    python:
        mono_with_character("답답함에 집을 뛰쳐나와 하염없이 길을 걸어도 내가 할 수 있는 건 없었다.")
        mono_with_character("배가 고프다.")
        mono_with_character("발이 시리다.")
        mono_with_character("모진 겨울 바람에 귀가 깨질 것만 같다.")
        mono_with_character("왜 나는 이렇게 징징 울며 걷는 것 말곤 할 수 있는 게 없을까?")
        handle_next_monologue()
    none ""
    with dissolve

    scene bg_sky
    oweon "나는 어떻게 해야 됩니까?"
    python:
        mono_with_character("누군가에게 물어도 대답이 없다.")
        handle_next_monologue()
    none ""
    oweon "나는 무얼 해야됩니까?"
    python:
        mono_with_character("여전히 대답이 없다.")
        handle_next_monologue()
    none ""
    with fade

    scene bg_village
    oweon "밥 좀 주이소"
    show ms_image:
        xpos 550
        ypos 100
    ms "너 뉘집 자식이고?"
    ms "지금이 어느 때 하고 밥을 달라 카노...?"
    ms "에휴 꼴을 보니 무슨 일이 있었는지는 모르겠지마는... 쪼매 기다려 보그래이"
    ms "다시는 오지 말그래이"
    ms "우리 집도 양식이 떨어져 간다. 느그 줄 밥 없대이"
    hide ms_image
    python:
        mono_with_character("바가지에 담긴 찬밥을 보니 단숨에 먹어치우고 싶다.")
        handle_next_monologue()
    none ""
    oweon "......."
    python:
        mono_with_character("문득 울고 있던 어머니가 떠올랐다.")
        handle_next_monologue()
    none ""
    with fade

    scene bg_winter_mountain
    show mother_image:
        xpos 550
        ypos 100
    mother "니 어데서 이걸 얻어 갖고 왔노?"
    hide mother_image
    python:
        mono_with_character("깜짝 놀란 어머니는 노하기는 했지만 눈가에 눈물을 글썽이고 있었다.")
        handle_next_monologue()
    none ""
    with fade

    none "며칠 후"
    show tired_oweon_image at myfade_character:
        xpos 550
        ypos 100
    python:
        mono_with_character("배라도 곯지 않아야 빨리 낳지 않을까 싶어 며칠을 밥 구걸하고 다녔지만")
        mono_with_character("겨울 바람에 마을 사람들의 곳간마저 꽁꽁 닫아버렸다. 이젠 어쩌지")
        handle_next_monologue()
    none ""
    unknown "사시오_! 사시오_!"
    python:
        mono_with_character("저건 뭐지?")
        handle_next_monologue()
    oweon ""
    hide tired_oweon_image
    scene bg_winter_road
    show kim_standing_image:
        xpos 550
        ypos 100        
    unknown "튼튼한 목침도 있고 어염도 있습니다"
    hide kim_standing_image
    show smile_oweon_image:
        xpos 550
        ypos 100
    oweon "세상에 처음보는 물건이 가득하다."
    oweon "저건 과자인가? 인삼도 있어!"
    hide smile_oweon_image
    oweon "저거면 아부지도 씻은듯이 일어나실텐데"
    oweon "한 푼도 없으니 인삼은 커녕 개떡하나 사지도 못하네"
    python:
        mono_with_character("처음 보는 물건이 가득하니 신기하기도 했지만")
        mono_with_character("무엇보다 그 사람은 이 세상에 근심 걱정이라곤 없고")
        mono_with_character("그저 기쁨만 맛보며 사는 사람 같아 눈을 뗄 수 없었다.")
        mono_with_character("그 사람은 며칠 동안 근처를 돌아다니더니 어느 날 사라져 버렸다.")
        mono_with_character("나는 그가 다시 나타난다면 그처럼 여기저기 다닐 수 있는 기술이 무엇인지,")
        mono_with_character("어떻게 하면 나도 그렇게 될 수 있는지")
        mono_with_character("묻고 싶었다.")
        handle_next_monologue()
    none ""
    with dissolve
    scene black
    mother "우짜고, 우짜고... 우리 영근이를 우짜고"
    python:
        mono_with_character("영근이가 굶주림 끝에 쓰러진 것이다.")
        handle_next_monologue()
    none ""

    scene bg_winter_road_afternoon
    python:
        mono_with_character("앓은 동생의 머리를 만지며 한편으로는")
        mono_with_character("아버지를 보살피는 어머니를 보다가")
        mono_with_character("무작정 문을 박차고 뛰어 나왔다.")
        mono_with_character("무슨 말씀이라고 받고자 할아버지가 계시는 마을에 갔지만")
        mono_with_character("별 도리가 없어 약방이 있는 안강읍까지 쉬지 않고 뛰었다.")
        mono_with_character("넓은 들에 다다르자 귀를 도려내는 듯한 북쪽 바람이 맹렬히 쓸고 지나간다.")
        mono_with_character("빨갛게 오른 두 뺨을 이따금 문지르며 약방에 다다라 문을 두들겼다.")
        handle_next_monologue()
    none ""
    show tired_oweon_image:
        xpos 550
        ypos 100
    oweon "사람 살리시소! 내 동생 살려주시소!"
    hide tired_oweon_image
    show doctor_image:
        xpos 550
        ypos 100
    doctor "아니 이게 무슨...?"
    hide doctor_image
    show tired_oweon_image:
        xpos 550
        ypos 100
    oweon "내 동생 좀 살려주시소"
    oweon "열이 펄펄 끓고 배는 짜부러지고"
    hide tired_oweon_image
    show doctor_image:
        xpos 550
        ypos 100
    doctor "얘야, 얘야. 진정하고 찬찬히 말해 보그라"
    python:
        mono_with_image("어디 뉘집 자식일꼬?", doctor, "doctor_edit_image")
        mono_with_image("하는 말이 기특한데...", doctor, "doctor_edit_image")
    hide doctor_image
    show tired_oweon_image:
        xpos 550
        ypos 100
    oweon "입은 바싹 마르고.. 또.. 또.."
    hide tired_oweon_image
    show doctor_image:
        xpos 550
        ypos 100
    python:
        mono_with_image("말하는 증상도 그렇고 보아하니 필시 제대로 먹지 못해서 그런게로구나", doctor, "doctor_edit_image")
        mono_with_image("분명 돈이라곤 한 푼도 없을테지", doctor, "doctor_edit_image")
    doctor "울지도 보채지도 않고 멍하니 쳐다만 보고"
    doctor "오냐, 네 녀석 돈이 없다고 해고 인술을 다루는 마당에 한 번쯤 봐주지 못할 쏘냐?"
    hide doctor_image
    with myfade_5

    scene bg_winter_road_night 
    doctor "퍼뜩 가서 달여주그라"
    doctor "낫거든 한번 더 오그라"
    python:
        mono_with_character("중천에 떠 있던 해는 어느 새 저물어 갔다.")
        mono_with_character("북풍은 아까보다도 한층 더 피부에 아렸다.")
        mono_with_character("얼마쯤 왔을까?")
        mono_with_character("이러다가 동생에게도 약도 갖다주지 못하고 죽을 것 같았다.")
        mono_with_character("죽을 수 없다")
        mono_with_character("뛰어야 한다")
        mono_with_character("냇물을 건너고 북풍을 맞으며 견뎠으나")
        mono_with_character("고픈 배는 더는 뛸 힘을 마련해 주지 않았다.")
        handle_next_monologue()
    none ""
    oweon "......"
    with myfade_1
    
    scene bg_winter_road_night 
    show ms_image at myfade_character:
        xpos 550
        ypos 100
    villa "일나라! 일나라!"
    oweon "……"
    villa "아무리 두드려도 정신을 못차리니 원…"
    villa "아니 가만 있어보자."
    villa "어디서 본 얼굴인데?"
    villa "아차, 김한중의 자식이 아닌가!"
    villa "품 안에 약봉지고 하며 요 조그만 것이 어찌…"
    hide ms_image
    with myfade_1

    scene bg_winter_mountain_night
    show ms_image at myfade_character:
        xpos 550
        ypos 100
    villa "원근이를 업고 왔소!"
    villa "누가 좀 내다 보소"
    hide ms_image
    show mother_image at myfade_character:
        xpos 550
        ypos 100
    mother "어메! 이게 우짠 일이고"
    mother "어데 갔다 왔노, 니?"
    hide mother_image
    show ms_image:
        xpos 550
        ypos 100
    villa "가슴 팍에 약 지은게 있습디더."
    hide ms_image
    show mother_image:
        xpos 550
        ypos 100
    mother "약이예?"
    mother "이놈아가 어데 가서 구해놨노"
    mother "동생이 앓는다꼬 아침에 안 나갔는교"
    hide mother_image
    show ms_image:
        xpos 550
        ypos 100
    villa "허 참!"
    villa "두구 보소."
    villa "죽을 때 까지 이 형제는 의가 좋을거요"
    hide ms_image
    with myfade_1

    scene bg_indoor
    show oweon_image at myfade_character:
        xpos 550
        ypos 100
    oweon "니 다 낫나?"
    hide oweon_image
    show young_image at myfade_character:
        xpos 550
        ypos 100
    young "다 낫다."
    hide young_image
    show oweon_image:
        xpos 550
        ypos 100
    oweon "……"
    oweon "됐다."
    with myfade_1

    scene bg_winter_road
    show oweon_image
    oweon "빌어묵을!"
    oweon "배 좀 잔뜩 부르게 먹을 수 없나"
    oweon "그놈의 돈 좀 있을 수 없나"
    oweon "배부르고 돈이 잔뜩 있으면 세상 부러울 것 없겠다."
    oweon "어떻게 하면 그렇게 될 수 있나"
    oweon "어?"
    oweon "저 사람은?"
    hide oweon_image
    show kim_standing_image at myfade_character:
        xpos 550
        ypos 100
    oweon "안녕하십니꺼"
    unknown "오냐, 니가 누구지?"
    oweon "조오기 안 사는교"
    unknown "오, 너희 아버지가 아프다고 그랬던가?"
    oweon "예"
    unknown "다 나았나?"
    oweon "아니예"
    unknown "안됐구나"
    oweon "……"
    oweon "아저씨는 장사 다니지예?"
    unknown "그렇지. 장사다니지."
    unknown "왜 그러느냐?"
    oweon "….."
    unknown "서당에 다니냐?"
    oweon "안 다닙니더."
    unknown "그럼 뭘 하냐?"
    oweon "아버지가 편찮아서 아무것도 몬 합니더."
    unknown "네 나이 때는 공부를 해야 하는 법인데…"
    oweon "…"
    oweon "지도 장사하는거 배울 수 있십니꺼?"
    unknown "니가?"
    oweon "배우고 싶십니더."
    oweon "좀 가르쳐 주소"
    unknown "어떻게 가르치니?"
    oweon "저를 예,"
    oweon "아저씨가 데려가 주소"
    unknown "나는 먼 데서 왔다."
    unknown "충청도까지 가야 돼."
    unknown "너를 어찌 데리고 가니"
    oweon "갈 수 있십니더!"
    oweon "장사 배우가지고, 돈 벌믄 다시 이곳으로 오겠십니더"
    unknown "허…"
    oweon "데려가 주이소, 예?"
    unknown "저렇게 조그만 것이 무슨 결심을 그렇게 단단히 했을까"
    with dissolve
    scene bg_sky_mountain
    hide kim_standing_image with dissolve
    with myfade_5

    scene bg_sky_mountain
    show kim_standing_image at myfade_character:
        xpos 550
        ypos 100
    unknown "야야, 야야…."
    unknown "네 이름이 뭐지?"
    hide kim_standing_image
    show oweon_image at myfade_character:
        xpos 550
        ypos 100
    oweon "김원근입니더"
    hide oweon_image
    show kim_standing_image:
        xpos 550
        ypos 100
    unknown "어디 김씬가?"
    hide kim_standing_image
    show oweon_image:
        xpos 550
        ypos 100
    oweon "김해 김씨요"
    hide oweon_image
    show kim_standing_image:
        xpos 550
        ypos 100
    unknown "오, 나하구 같은 집안이로구나."
    unknown "일가야."
    unknown "우리 집은 충청북도 청원군이여." 
    unknown "일가를 데려왔다구 할 테니 너두 그렇게 대답해야 된다"
    hide kim_standing_image
    show oweon_image:
        xpos 550
        ypos 100
    oweon "예"
    hide oweon_image
    show kim_smile_image at myfade_character:
        xpos 550
        ypos 100
    kook "그리고 내 이름은 국선이다"
    hide kim_standing_image with dissolve
    with myfade_5

    scene bg_tavern
    show kim_standing_image at myfade_character:
        xpos 550
        ypos 100
    kook "암만 해두 너희 집에 얘기두 안 하구 데려가는게 걸리는 구나"
    kook "도루 내려갈래?"
    kook "갈라면 내 데려다 주구"
    hide kim_standing_image
    show sulk_oweon_image at myfade_character:
        xpos 550
        ypos 100
    oweon "안갑니더"
    hide sulk_oweon_image
    show kim_standing_image:
        xpos 550
        ypos 100
    kook "오백오십리나 가야 한다." 
    kook "그래두 따라 올라 갈래?"
    hide kim_standing_image
    show sulk_oweon_image:
        xpos 550
        ypos 100
    oweon "예"
    hide sulk_oweon_image
    show kim_standing_image:
        xpos 550
        ypos 100
    kook "그 대신 다리가 아프다거나 아까처럼 주저 앉아 울거나 하면 난 모른다."
    kook "그땐 나 혼자 그냥 가버릴 테야"
    hide kim_standing_image
    show smile_oweon_image:
        xpos 550
        ypos 100
    oweon "예!"
    hide smile_oweon_image wity dissolve
    with myfade_5


    scene black
    none "청원군 남이면 외천리"
    with myfade_2

    scene bg_kim_house
    show kim_standing_image at myfade_character:
        xpos 550
        ypos 100
    kook "집안 아인데, 부탁을 받고 데려왔어"
    hide kim_standing_image with dissolve
    with myfade_2
    
    scene bg_kim_house
    show oweon_image at myfade_character:
        xpos 550
        ypos 100
    python:
        mono_with_character("국선 아저씨는 넉넉한 형평이 아닌데도 불구하고 우선 나를 서당부터 보냈다.")
        mono_with_character("행상을 가서 벌어 오는데 큰 재미를 보지 못하는 경우가 많았다.")
        mono_with_character("그래서 서당에 허투로 다닐 수 없었다.")
        mono_with_character("아침에 읽어 주면 저녁에 새기고, 외우고, 저녁에 배운 것은 밤에 모조리 터득했다")
        mono_with_character("천자문도 동몽선습도 남보다 빨리 떼니 훈장과 국선 아저씨의 칭찬에 더욱이 신이 났다")
        handle_next_monologue()
    none ""
    hide oweon_image
    show smile_oweon_image at myfade_character:
        xpos 550
        ypos 100
    none ""
    hide smile_oweon_image with dissolve
    with myfade_2

    scene bg_school
    python:
        mono_with_character("하지만 반년이 지났을 무렵,")
        mono_with_character("국선 아저씨의 형편이 갑자기 기울어져 나는 훈장의 서생으로 맡겨졌다")
        mono_with_character("다행히 밥은 얻어먹었으나 가진 것이 없어")
        mono_with_character("종이 장수가 와도 바라다 보고만 있어야 했다.")
        mono_with_character("그나마 학우들이 한두 장 씩 나눠주는 종이를 새까맣게 되도록 쓰고 또 썼다.")
        mono_with_character("그렇게 남보다 먼저 당시(唐詩)를 읽고 사략(史略) 초 권을 터득한지 1년이 지날 무렵")
        mono_with_character("돌봐 주던 훈장마저 병으로 세상을 떠나 내가 자연스레 선생 격이 되었다.")
        mono_with_character("힘들었지만 17명의 학우들과 같이 기거하며 정답게 공부했기에 버틸 수 있었다")
        mono_with_character("그러던 어느날 경주로 행상을 다녀온 국선 아저씨가 나를 조용히 불러냈다")
        handle_next_monologue()
    none ""
    kook "원근아"
    oweon "예, 아저씨."
    kook "맘 단단히 먹고 들어라."
    oweon "……?"
    with myfade_2
    scene black
    kook "어머니가 작고 하셨단다."
    with myfade_5


    scene bg_school
    show student_image
    stu_1 "형, 꼭 가야되나?"
    hide student_image
    hide oweon_image with dissolve
    with myfade_2

    scene bg_school
    show cry_oweon_image at myfade_character:
        xpos 550
        ypos 100
    oweon "어머니 죄송해요"
    oweon "어떻게든 돈을 벌어 한아름 안고 돌아가고 싶었어요"
    oweon "그런데 아직 시작도 못했는데"
    oweon "병든 아버지랑 어린 영근이는 어쩌나"
    hide cry_oweon_image with dissolve
    with myfade_2

    scene bg_school
    show oweon_image at myfade_character:
        xpos 550
        ypos 100
    oweon "미안타"
    hide oweon_image
    show student_two_image
    stu_2 "야야 이거 받아라"
    hide student_two_image
    show oweon_image
    oweon "이게 뭔데?"
    hide oweon_image
    show student_image
    stu_1 "우리끼리 조금씩 모았어."
    hide student_image
    show student_two_image
    stu_2 "어른들이 그랬어!"
    stu_2 "돈이 있어야 돈이 모인데!"
    hide student_two_image
    show oweon_image
    oweon "……"
    oweon "고맙다"
    hide oweon_image with dissolve
    python:
        mono_with_character("같이 공부하던 학우들은 내가 떠나는 것을 서운해 하며 엽전 석 냥 석 돈을 모아 주었다.")
        mono_with_character("나 역시 아쉬움이 남았지만 오래 머물면 미련만 더 남을것 같았다")
        mono_with_character("학우들이 준 그 돈을 허리에 차고 그대로 청주로 떠났다")
        handle_next_monologue()
    none ""
    with myfade_2
    
    scene black
    none "며칠 후"
    with myfade_2

    scene bg_market
    show Merchant_image:
        xpos 550
        ypos 100
    tr "어린 녀석이 무슨 장사냐!"
    tr "집에 가서 주는 밥이나 먹어라!"
    hide Merchant_image
    python:
        mono_with_character("청주로 올라와 장날 장터를 이리저리 헤매다")
        mono_with_character("기름집에 들어가 부탁을 하고 하룻밤을 지냈다")
        mono_with_character("기름집에 있다 보니 문득 이 많은 기름을 사 가지고")
        mono_with_character("이 마을 저 마을 다니며 팔아 볼까 생각이 들었다")
        mono_with_character("처음에는 몸이 고되어도 몇 푼 생기는 재미가 있었고")
        mono_with_character("약간의 밑천이 생겨 국선 아저씨처럼 잡화를 사서 장마다 돌아다녔다")
        mono_with_character("하지만 2년 동안 이곳저곳 돌며 장돌뱅이 생활을 해도")
        mono_with_character("나이가 어려 핀잔만 받기 일수였다.")
        handle_next_monologue()
    none ""
    show oweon_image at myfade_character:
        xpos 550
        ypos 100
    oweon "오늘따라 국선 아저씨가 더 생각난다."
    oweon "잘 계실까?"
    oweon "아저씨를 따라 온 것도 5년 가까이 되었네"
    oweon "경주에서 충청도로 올라오는 동안에도 아저씨는 물건 참 잘 파셨는데"
    oweon "어? 그러고 보니……"
    oweon "아저씨가 파는 물건들이 지금 보면 그렇게 별난 물건들은 아니었어"
    oweon "마을마다 팔리는 값도 달랐고 사가는 것도 다 달랐어"
    oweon "그래."
    oweon "요 근처를 뱅뱅 돌 게 아니라 좀 멀치감치 왔다 갔다 해 보자"
    hide oweon_image with dissolve
    with myfade_5

    return