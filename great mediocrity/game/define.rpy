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
define unkown = Character('???', color = "#ffffff")
define none = Character('', color = "#ffffff")
define han = Character('김한중', color = "#ffb700")
define boss = Character('동학군 두목', color = "#ffffff")
define burden = Character('동학군', color = "#ffffff")
#1장 2절                        #씬1 주인공 김한중, 씬2 주인공 어린 김원근만 주황색
define oweon = Character('어린 김원근', color = "#ffb700")
define ms = Character('아낙네', color = "#ffffff")
define mother = Character('어머니', color = "#ffffff")
define doctor = Character("의원", color = "#ffffff") 

##배경
#1장 1절
image bg_burning_building = "images/background/chap1_1/burning_building.png" #활활
image bg_burning = "images/background/chap1_1/burning.jpg"
image bg_yard = "images/background/chap1_1/yard.png" 

#1장 2절
image bg_winter_mountain = "images/background/chap1_2/winter_mountain.png"
image bg_winter_mountain_night = "images/background/chap1_2/winter_mountain_night.png"
image bg_fpp = "images/background/chap1_2/first_person_perspective.png"
image bg_sky = "images/background/chap1_2/sky.png"
image bg_village = "images/background/chap1_2/village.png"
image bg_winter_road = "images/background/chap1_2/winter_road.png"
image bg_winter_road_afternoon = "images/background/chap1_2/winter_road_afternoon.png"
image bg_winter_road_night = "images/background/chap1_2/winter_road_night.png"


##

##인물 이미지
#1장 1절
image han_image_bound = "images/character/chap1_1/han_bound.png"
image han_image_loose =  "images/character/chap1_1/han_loose.png"
image boss_image = "images/character/chap1_1/boss.png"
image group_image = "images/character/chap1_1/group.png"
image ch1_extra1_image = "images/character/chap1_1/ch1_extra1.png"
image ch1_extra2_image = "images/character/chap1_1/ch1_extra2.png"
image ch1_extra3_image = "images/character/chap1_1/ch1_extra3.png"
image Donghak_scene_image = "images/character/chap1_1/Donghak_scene.png"

image boss_dark_image = im.MatrixColor(im.FactorScale("images/character/chap1_1/boss.png", 0.3), im.matrix.brightness(-0.3))
image han_image_bound_dark_image = im.MatrixColor(im.FactorScale("images/character/chap1_1/han_bound.png", 0.3), im.matrix.brightness(-0.3))
image han_image_loose_dark_image = im.MatrixColor(im.FactorScale("images/character/chap1_1/han_loose.png", 0.3), im.matrix.brightness(-0.3))


#1장 2절
image standing_oweon_image = "images/character/chap1_2/standing_oweon.png"
image dad_son_image = "images/character/chap1_2/dad_son.png"
image mother_image = "images/character/chap1_2/mother.png"
image tired_oweon_image = "images/character/chap1_2/tired_oweon.png"
image smile_oweon_image = "images/character/chap1_2/SmileImage.png"
image sulk_oweon_image = "images/character/chap1_2/SulkImage.png"
image kim_standing_image = "images/character/chap1_2/KimStanding.png"
image kim_smile_image = "images/character/chap1_2/KimSmile.png"
image doctor_image = "images/character/chap1_2/Doctor.png"
image doctor_edit_image = "images/character/chap1_2/Doctor_edit.png"
image villeger_image = "images/character/chap1_2/villager.png"


image 40_oweon = "images/character/chap3_1/40_oweon.png"

##

## 사용자 지정 페이드 인/아웃
define myfade_3 = Fade(0.3, 10.5, 0.0)
define myfade_0 = Fade(0.5, 10.5, 0.0)   #0.5초간 페이드
define myfade_1 = Fade(2.0, 2.0, 0.0)    #2초간 페이드(씬 전환)
define myfade_5 = Fade(5.0, 5.0, 0.0)    #5초간 페이드(절 전환)
init:
    transform myfade_character:    #등장인물 페이드 인
            alpha 0.0              # 처음엔 완전히 투명하게 시작
            linear 1.0 alpha 1.0

    #transform myfade_out_1:        #등장인물 페이드 아웃
    #        alpha 1.0              # 처음엔 완전히 보이는 상태에서 시작
    #        linear 1.0 alpha 0.0 
    
# 어두운 오버레이 이미지 정의
image dark_overlay = Solid("#000000")  # 50% 투명한 검은색


