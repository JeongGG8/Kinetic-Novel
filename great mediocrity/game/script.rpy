# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"

# 게임에서 사용할 캐릭터를 정의합니다.
define unkown = Character('???', color = "#4764ce")
define none = Character('', color = "#ffffff")
define han = Character('김한중', color = "#012482")
define boss = Character('동학군 두목', color = "#016583")
define burden = Character('동학군', color = "#015625")

image bg_burning_building = "images/background/burning_building.png"
image bg_yard = "images/background/yard.png"
image bg_burning = "images/background/burning.jpg"


image han_image_bound = im.FactorScale("images/character/han_bound.png", 0.3, )
image han_image_loose =  im.FactorScale("images/character/han_loose.png", 0.3)
image boss_image = im.FactorScale("images/character/boss.png", 0.3)


# 여기에서부터 게임이 시작합니다.
#1장 1절

label start:
    scene black
    none "1894년"
    unkown "불이야!"
    unkown "불이야앗!!"

    play sound "audio/door_sound.mp3"

    scene bg_burning_building
    unkown "네놈이 사장책이렸다! 순순히 이르는 대로 따라야지 반항하면 큰 코 다칠 줄 알아라!"
    play sound "audio/hit_sound.mp3"
    with dissolve

    scene bg_yard
    show boss_image
    boss "네가 이 곳의 사장책이냐"
    hide boss_image
    show han_image_bound:
        xpos 400
        ypos 100
    han "......그렇다."
    hide han_image_bound
    show boss_image
    boss "네가 왜 포박되었는지 아느냐?"
    hide boss_image
    show han_image_bound:
        xpos 400
        ypos 100
    han "내가 묻고 싶은 말이아. 대체 어디서 온 누구냐? 뭣 때문에 소중한 나라의 곡식에 불을 지르고 이와 같이 소동을 피우는가!?"
    hide han_image_bound
    show boss_image
    boss "네 말이 뜻 밖에도 시원하구나. 세상이 어찌 되었는지 들은바 없나?"
    hide boss_image
    show han_image_bound:
        xpos 400
        ypos 100
    han "없다!"
    hide han_image_bound
    show boss_image
    boss "어리석구나. 이곳 농민들한테 들으니 너는 우직하고 착해빠진 사창으로, 조정에서 하라는 대루만 하는 놈이라...."
    boss "이제 그 어리석음을 깨우쳐 주시 위해서 이야기해 줄기니 소상히 듣거라."
    boss "저기있는 곡식은 누가 먹을 거였나?"
    hide boss_image
    show han_image_bound:
        xpos 400
        ypos 100
    han "내 알 배 아니다. 조정에 바칠 뿐이다."
    hide han_image_bound
    show boss_image
    boss "나라를 생각하는 놈들이냐? 백성을 걱정하는 무리들이냐? 아니였제? "
    boss "제놈들 배창자 채우고 갖은 호강 다 하구, 주지육림에 몸을 담아 썩어 가는 출 모르는  데 썼단 말이다!"
    boss "동학군은 일어섰다. 불의를 쳐부술 것이다. 너는 그 불의의 꼭두각시 노릇을 한 놈, 따라서 형을 받아야 마땅하다!"
    hide boss_image
    with dissolve

    scene black
    han "모두 옳은 소리다, 양반이 관직을 얻어 3년만 벼슬을 누리면 자손 대대로 만복을 누린다. 그만큼 양반은 백성들을 착취했고, 심지어는 죽기까지 했다."
    han "일찍 부모님을 여의고 간신히 간신히 살아오다가 이제 겨우 터를 잡아 끼니 굶지 않는 신세가 되었는제..... 이제 마지막인가. 이걱이 모든 것의 끝장인가."
    with dissolve
    scene bg_yard
    show boss_image
    boss "......"
    boss "김한중"
    hide boss_image
    show han_image_bound:
        xpos 400
        ypos 100
    han ".....?"
    hide han_image_bound
    show boss_image
    boss "네가 김한중이라 하는 것은 틀림이 없겠제?"
    hide boss_image
    show han_image_bound:
        xpos 400
        ypos 100
    han "틀림없소"
    hide han_image_bound
    show boss_image
    boss "저자를 이리 끌어내리고 포승을 풀어라!"
    burden "어째서 풀어줍니까?"
    boss "풀어주라 하잖나!"
    hide boss_image
    with dissolve

    scene bg_burning
    show boss_image
    boss "일어나그라!" 
    boss "그대로 듣거라! 김한중은 우리가 동학군이라는 것을 아느냐?"
    hide boss_image
    show han_image_loose:
        xpos 400
        ypos 100
    han "예."
    hide han_image_loose
    show boss_image 
    boss "동학군은 불의를 꺾자고 하다가 너를 잡았다. 그런데 근방 사람들 얘기를 들으니, 네 천성이 어질고 착실하여 비록 상부의 명령을 따르기는 했지만도, 네 멋대로 백성을 괴롭히지는 않았다는 것을 알았다. 목숨만은 부지하게 해줄테니 당장 이곳을 떠야 할 것이다."
    hide boss_image
    show han_image_loose:
        xpos 400
        ypos 100
    han ".....!!"
    hide han_image_loose
    show boss_image
    boss "떠라! 오늘 밤 안으로 멀리멀리 떠라!"
    hide boss_image
    with dissolve

    return

label chap1:
    scene black
    none "경주군 안강면 어느 산 속"