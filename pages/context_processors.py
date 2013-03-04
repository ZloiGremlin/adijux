from models import Block, Menu
from room.models import Room

def block(request):
    l = request.session.get('lang','ru')
    bl = Block.objects.filter(translations__language_code=l)
    blocks = {}
    for item in bl:
        blocks.update({item.name:item.text})
    return {'blocks': blocks}

def top_menu(request):
    l = request.session.get('lang','ru')
    all = Menu.objects.all()
    menu = all.filter(position='top', parent=None)
    botmenu = all.filter(position='bottom', parent=None)
    return {'topmenu': menu, 'bottommenu': botmenu}

def subroom(request):
    all = Room.objects.all()
    return {'subroom': all}
