from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.animation import Animation
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle, Line, Ellipse
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle, StencilPush, StencilUse, StencilPop, StencilUnUse, RoundedRectangle
from kivy.uix.scrollview import ScrollView
from kivy.effects.scroll import ScrollEffect
from kivy.uix.gridlayout import GridLayout
from kivy.uix.behaviors import DragBehavior

class NumberCircle(Widget):
    def __init__(self, number, **kwargs):
        super(NumberCircle, self).__init__(**kwargs)
        self.number = number
        self.size = (25, 25)  # Kichraytirilgan doira o'lchami

        with self.canvas:
            Color(1, 1, 1, 1)  # Oq rang
            self.circle = Ellipse(pos=self.pos, size=self.size)

        # Raqamni yaratish va joylashtirish
        self.label = Label(text=str(number), color=(0, 0, 0, 1), font_size=14, size_hint=(None, None))
        self.label.size = self.label.texture_size
        self.add_widget(self.label)

        # Pos va size yangilansa, doira va raqamni yangilash
        self.bind(pos=self._update_circle)

    def _update_circle(self, *args):
        self.circle.pos = self.pos
        self.label.center = self.center  # Raqamni doira ichiga joylashtirish

class RoundIcon(Widget):
    def __init__(self, **kwargs):
        super(RoundIcon, self).__init__(**kwargs)

        # Rasm burchaklarini yumaloqlash uchun kerakli o'lcham va pozitsiyani yangilash
        with self.canvas:
            StencilPush()

            # Rasmning burchaklarini yumaloqlash uchun mask yaratish
            Color(1, 1, 1, 1)
            self.rounded_rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[100, 100])

            StencilUse()

        # Rasmni qo'shish
        self.icon_image = Image(source='./image/bbb.jpg', allow_stretch=True, keep_ratio=False)
        self.icon_image.size = self.size
        self.icon_image.pos = self.pos
        self.add_widget(self.icon_image)

        # Stencilni yopish
        with self.canvas:
            StencilUnUse()
            StencilPop()

        self.bind(pos=self.update_icon_pos, size=self.update_icon_pos)

    def update_icon_pos(self, *args):
        # Markazga joylashish
        self.rounded_rect.pos = self.pos
        self.rounded_rect.size = self.size
        self.icon_image.pos = self.pos
        self.icon_image.size = self.size
        
class SplashScreen(Widget):
    def __init__(self, **kwargs):
        super(SplashScreen, self).__init__(**kwargs)

        # Ekran o'lchamlarini olish
        Window.size = (360, 640)  # Masalan, standart mobil telefon o'lchami
        self.size = Window.size

        # Orqa fon uchun rasm qo'shish
        self.background_image = Image(source='./image/bg_test.jpg', allow_stretch=True, keep_ratio=False)
        self.background_image.size = self.size
        self.background_image.pos = self.pos
        self.add_widget(self.background_image)

        # Ilova ikonkasini doira shaklida qo'shish
        self.icon = RoundIcon(size=(200, 200))
        self.add_widget(self.icon)

        # Orqa fon rasmni o'lchamini va joylashuvini yangilash
        self.bind(size=self._update_rect, pos=self._update_rect)
        self._update_rect(self, None)

    def _update_rect(self, instance, value):
        self.background_image.size = self.size
        self.background_image.pos = self.pos

        # Ikonkaning markazda joylashuvi
        self.icon.center_x = self.center_x
        self.icon.center_y = self.center_y



class MainScreen(Widget):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
         # green_line atributini yarating
        self.green_line = Line()
        self.green_line1 = Line()
        
        # Right section Layout
        self.right_section = BoxLayout(orientation='vertical')
        self.add_widget(self.right_section)
        
        # Orqa fon uchun Rectangle
        with self.canvas:
            # Top section background (Blue)
            Color(20 / 255, 92 / 255, 215 / 255, 1)
            self.top_section = Rectangle(pos=(0, self.height - 95), size=(self.width, 95))

            # Left vertical section background (Green)
            Color(0, 255, 0)
            self.left_section = Rectangle(pos=(0, 0), size=(self.width * 0.3, self.height - 95))

            # Middle vertical section background (Red)
            Color(1, 0, 0)  # Ranglarni to'g'ri belgilang (0-1 oralig'ida)
            self.middle_section_bg = Rectangle(pos=(self.width * 0.3, 0), size=(self.width * 0.4, self.height - 95))

            # Green section's horizontal white line
            Color(1, 1, 1, 1)
            self.green_line.points = [0, self.height * 2 / 3, self.width * 0.3, self.height * 2 / 3]
            
            # White vertical lines for section separation
            self.vertical_line1 = Line(points=[self.width * 0.3, 0, self.width * 0.3, self.height - 95], width=1.5)
            self.vertical_line2 = Line(points=[self.width * 0.7, 0, self.width * 0.7, self.height - 95], width=3)
            
            # Oq chiziq - faqat yashil bo'lim kengligida
            Color(1, 1, 1, 1)
            green_section_width = self.width * 0.3
            y_pos = self.height - 170
            self.green_line1 = Line(points=[0, y_pos, green_section_width, y_pos], width=1.5)
            
            # Right section background (Yellow)
            Color(1, 1, 0, 1)  # Sariq rang RGBA
            self.right_section_bg = Rectangle()
#====================================================================== 

        # Rasmlarni joylash
        self.image_layout = GridLayout(cols=1, size_hint=(None, None), spacing=20, padding=[10, 10, 10, 10])
        self.image_layout.size = (self.width * 0.28, self.height / 2)
        self.image_layout.pos = (self.width * 0.71, self.height / 3)

        # 4 ta rasm qo'shish
        image_paths = ['./image/10/1.png', './image/10/2.png', './image/10/3.png', './image/10/4True.png']
        for path in image_paths:
            img = Image(source=path, allow_stretch=True, keep_ratio=False, size_hint=(None, None), size=(100, 110))
            self.image_layout.add_widget(img)

        self.add_widget(self.image_layout)
#-======================================================


        # "Variantlar:" matnini qo'shish
        self.add_variant_label()
    
        # Oyna kengligi o'zgarganda chiziqni yangilash uchun bind qilish
        self.bind(size=self.update_rect)
    
        # Numbers and test quiz label
        self.numbers = []
        self.add_numbers_between_lines()
    
       # Yangi menyu bloklarini qo'shish
        # self.create_multiple_blocks()

        
        # Clippingni yangilash
        self.bind(size=self.update_rect, pos=self.update_rect)
    
        self.label = Label(text="test quiz", font_size=40, size_hint=(None, None), color=(1, 1, 1, 1))
        self.add_widget(self.label)
        self.label.center_x = self.center_x
        self.label.y = self.height - 62 - 50  # Above the numbers
    
        # ScrollView qo'shish (left section uchun)
        self.scroll_view = ScrollView(size_hint=(None, None), size=(self.width * 0.3, self.height - 95), 
                                    pos=(0, 0), do_scroll_x=False, do_scroll_y=True)
    
        self.text_layout = BoxLayout(orientation='vertical', size_hint_y=None, spacing=2)
        self.text_layout.bind(minimum_height=self.text_layout.setter('height'))
        self.scroll_view.add_widget(self.text_layout)

        # Matnlarni ScrollView ichida ko'rsatish
        self.texts = [
            ("1.Kumushbibi Zaynablar\nibo hayo timsoli\nQani ayting qay asarda\ntoping zukko misoli", 10),
            ("2.Anvar Ra’no berilgan\nTaqdiri keltirilgan\nAytingchi bu qay asar\nJavobini kim aytar", 10),
            ("3.Yaxshilik yomonlikni\nbu asarda bilamiz\nAsadbek timsolini\nqay asarda ko‘ramiz", 10),
            ("4.Ushbu asar trelogiya\nMazmuni zo’r benihoya\nqani menga kim aytar\nBu qaysi mashhur asar?", 10),
            ("5.Ajdodimiz hayoti\nBitilgan jasorat\nO’zi mohir sarkarda\nBo’lgan qaysi asarda?", 10),
            ("6.Bu kitobni o’qisak\nBobur hayotidan darak\nYurt sog’inchi bitilgan\nQaysi asarda beshak?", 10),
            ("7.Farhod Shirin Layli Majnun\nqani ayting shu tobda\nbesh dostondan iborat\nAyting qaysi kitobda?", 10),
            ("8.Ma’naviyat sabog’in\nBeradi ushbu kitob\nQani bir oz o’ylab ko’r\nSo’ngra javobin top?", 10),
            ("9.Qalami o’tkir yozuvchi\nO’tkir Hoshimov bo’ladi\nEng sara asarlarin\nAyting kimlar biladi?", 10),
            ("10.Bolalikda barchamiz\nJuda sevib o’qiymiz\nBobo buvijonlardan\nMa’nosini o’qiymiz?", 10), 
        ]

        self.text_labels = []
        for text, font_size in self.texts:
            text_label = Label(text=text, font_size=font_size, halign='center', valign='middle', 
                            size_hint_y=None, height=75, color=(1, 1, 1, 1))
            text_label.bind(size=text_label.setter('text_size'))
            self.text_layout.add_widget(text_label)
            self.text_labels.append(text_label)
    
        # Gorizontal chiziqlarni raqamlar ustiga va ostiga joylashtirish
        self.add_horizontal_lines_for_numbers()
    
        self.add_widget(self.scroll_view)
    
#===============================-============-==========-====
    def on_size(self, *args):
        # O'lchamlarni yangilash
        self.right_section_bg.size = (self.width * 0.3, self.height - 95)
        self.right_section_bg.pos = (self.width * 0.7, 0)

        self.image_layout.size = (self.width * 0.28, self.height / 2)
        self.image_layout.pos = (self.width * 0.71, self.height / 3)  # Layoutni yuqoriroq qilish
###########################################################################################
    def add_block(self, parent, block_type='menu', block_color=(25 / 255, 156 / 255, 197 / 255, 1), block_y_offset=-167):
        # Blokni mavjud bo'lsa olib tashlaymiz
        if hasattr(self, block_type) and getattr(self, block_type) in parent.children:
            parent.remove_widget(getattr(self, block_type))

        # Blok o'lchamini va joylashuvini belgilaymiz
        block_width = self.width * 0.35
        block_height = 65

        # Yangi bo'lim (blok) yaratish
        block = BoxLayout(orientation='vertical', size=(block_width, block_height))

        # Blokning joylashuvini hisoblaymiz
        middle_section_x = self.width * 0.3
        block_x_pos = middle_section_x + (self.width * 0.4 - block_width) / 2
        block_y_pos = self.height + block_y_offset  # Qizil blokdan pastda joylashadi

        block.pos = (block_x_pos, block_y_pos)

        # Orqa fon rangini va burchaklarni belgilaymiz
        with block.canvas.before:
            Color(*block_color)  # Fonga kerakli rang berish
            block.rect = RoundedRectangle(size=block.size, pos=block.pos, radius=[(block.height * 0.1, block.height * 0.1)])

        block.bind(size=self.update_rect, pos=self.update_rect)

        # Agar bu menyu blok bo'lsa, matn qo'shamiz
        if block_type == 'menu':
            text = "1.Kumushbibi Zaynablar\nibo hayo timsoli\nQani ayting qay asarda\ntoping zukko misoli"
            label = Label(text=text, halign='center', valign='middle', font_size='11px')
            label.bind(size=label.setter('text_size'))  # Matnni o'rtaga joylash
            block.add_widget(label)

        # Blokni ota konteynerga qo'shamiz
        parent.add_widget(block)
        
        # O'zgaruvchiga blokni saqlaymiz
        setattr(self, block_type, block)
    
    
    def add_variant_label(self):
        # Label uchun BoxLayout yaratish
        self.variant_box = BoxLayout(orientation='vertical', padding=[20, 0, 20, 0], size_hint=(None, None),
                                    size=(self.width * 0.3, 100), pos=(self.width * 0.7, self.height / 2 + 237))

        # "Variantlar" matni uchun Label
        self.variant_label = Label(text="Variantlar:", font_size=20, color=(0, 0, 0, 1), halign='center', valign='middle')
        self.variant_label.bind(size=self.variant_label.setter('text_size'))  # Matnni o'rtasiga joylash

        # Labelni BoxLayout ichiga qo'shamiz
        self.variant_box.add_widget(self.variant_label)

        # BoxLayoutni ekranga qo'shamiz
        self.add_widget(self.variant_box)


    def add_numbers_between_lines(self):
        start_x = 60
        end_x = self.width - 60
        spacing = (end_x - start_x) / 9
        for i in range(1, 11):
            x_pos = start_x + (i - 1) * spacing
            y_pos = self.height - 91
            if len(self.numbers) >= i:
                self.numbers[i-1].pos = (x_pos, y_pos)
            else:
                number_circle = NumberCircle(i, pos=(x_pos, y_pos))
                self.numbers.append(number_circle)
                self.add_widget(number_circle)


    def add_horizontal_lines_for_numbers(self):
        # Gorizontal chiziqlarni faqat bir marta chizish, qayta yaratmaslik
        if not hasattr(self, 'upper_line'):
            with self.canvas:
                Color(1, 1, 1, 1)  # Oq rang
                # Chiziqlarni yaratish
                self.upper_line = Line(points=[0, self.height - 62, self.width, self.height - 62], width=1.5)
                self.lower_line = Line(points=[0, self.height - 95, self.width, self.height - 95], width=1.5)


    def update_rect(self, instance, *args):
        # Rasmning joylashuvini va o'lchamini yangilash
        instance.canvas.before.clear()  # Eski rasmni o'chirish
        with instance.canvas.before:
             self.bg_image = Rectangle(source='./image/1/2.png', size=instance.size, pos=instance.pos)
            
        # Agar 'rect' atributi bo'lsa, pos va size ni yangilash
        if hasattr(instance, 'rect'):
            instance.rect.pos = instance.pos
            instance.rect.size = instance.size

        # Chap tarafdan chiqadigan yashil menu oq chiziq
        if hasattr(self, 'green_line1'):
            self.green_line1.points = [0, self.height - 170, self.width * 0.3, self.height - 170]

        # Pushti blok uchun yangilanish
        if hasattr(self, 'new_right_block'):
            self.new_right_block.rect.pos = self.new_right_block.pos
            self.new_right_block.rect.size = self.new_right_block.size

        # Orqa fon (sariq) Rectangle ni yangilash
        if hasattr(self, 'right_section_bg'):
            self.right_section_bg.pos = (self.width * 0.7, 0)
            self.right_section_bg.size = (self.width * 0.3, self.height - 95)
        


        # Gorizontal chiziqlarni yangilash
        self.upper_line.points = [0, self.height - 62, self.width, self.height - 62]
        self.lower_line.points = [0, self.height - 95, self.width, self.height - 95]

        # Vertikal chiziqlarni yangilash
        self.vertical_line1.points = [self.width * 0.3, 0, self.width * 0.3, self.height - 95]
        self.vertical_line2.points = [self.width * 0.7, 0, self.width * 0.7, self.height - 95]

        # Bloklarni yangilash
        self.add_block(parent=self, block_type='menu')
        
        # Qismalarning yangi o'lchamlari va joylashuvi
        self.top_section.size = (self.width, 95)
        self.top_section.pos = (0, self.height - 95)

        self.left_section.size = (self.width * 0.3, self.height - 95)
        self.left_section.pos = (0, 0)

        self.middle_section_bg.size = (self.width * 0.4, self.height - 95)
        self.middle_section_bg.pos = (self.width * 0.3, 0)

        self.right_section_bg.size = (self.width * 0.3, self.height - 95)
        self.right_section_bg.pos = (self.width * 0.7, 0)

        # Labelni yangilash
        self.variant_box.size = (self.width * 0.3, 100)
        self.variant_box.pos = (self.width * 0.7, self.height / 2 + 237)

        # Raqamlar pozitsiyasini yangilash
        self.add_numbers_between_lines()

        # "Test quiz" labelini yangilash
        self.label.center_x = self.center_x
        self.label.y = self.height - 62 - 15

        # ScrollViewni yangilash
        self.scroll_view.size = (self.width * 0.3, self.height - 95)
        self.scroll_view.pos = (0, 0)


class MainApp(App):
    def build(self):
        self.root = BoxLayout()
        self.splash_screen = SplashScreen()
        self.root.add_widget(self.splash_screen)

        # Animatsiyani ishga tushirish
        Clock.schedule_once(self.start_animation, 1.5)

        return self.root

    def start_animation(self, *args):
        # Orqa fon va ikonkaning asta-sekin yo'q bo'lishi uchun animatsiya
        anim = Animation(opacity=0, duration=1.5)
        anim.bind(on_complete=self.load_main_screen)

        # Ikonkani va orqa fonni animatsiya qilish
        anim.start(self.splash_screen.icon)
        anim.start(self.splash_screen.background_image)

    def load_main_screen(self, *args):
        # SplashScreen tugagach, yangi menyuni ochish va fonni ko'k rang bilan to'ldirish
        self.root.clear_widgets()
        self.main_screen = MainScreen()
        self.root.add_widget(self.main_screen)

if __name__ == "__main__":
    MainApp().run()




