"""
Django settings for geodjango project.

Generated by 'django-admin startproject' using Django 4.2.11.
"""
import os
from pathlib import Path

# Define o diretório base do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# Chave secreta para uso no ambiente de desenvolvimento (não deve ser usada em produção)
SECRET_KEY = 'django-insecure-=3n62!vz@c2nfti0r5bfyf+0z2%zg3y%z6!#*f+olp!ydi=fo$'

# Ativa o modo debug (não recomendado para produção)
DEBUG = True

ALLOWED_HOSTS = []

if os.name == 'nt':
    VENV_BASE = os.environ['VIRTUAL_ENV']
    os.environ['PATH'] = os.path.join(VENV_BASE, 'Lib\\site-packages\\osgeo') + ';' + os.environ['PATH']
    os.environ['PROJ_LIB'] = os.path.join(VENV_BASE, 'Lib\\site-packages\\osgeo\\data\\proj') + ';' + os.environ['PATH']

# Definição das aplicações instaladas no projeto
INSTALLED_APPS = [
    'jazzmin',  # Customização do admin Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "django.contrib.gis",  # Suporte a funcionalidades GIS
    'django_extensions',  # Ferramentas adicionais para desenvolvimento
    # Aplicações de terceiros
    "rest_framework",  # Framework para criar APIs RESTful
    "rest_framework_gis",  # Extensões GIS para Django REST Framework
    "leaflet",  # Integração com a biblioteca de mapas Leaflet
    'django_ckeditor_5',  # Editor de texto avançado
    'crispy_forms',  # Estilização de formulários
    'crispy_bootstrap5',  # Integração do Crispy Forms com Bootstrap 5
    # Aplicações locais
    "markers",
    "posts",
    "autores",
    'tipografia',
    'sobre',
]

# Middlewares do Django para segurança, sessão, autenticação, etc.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

# Configuração do URL principal do projeto
ROOT_URLCONF = 'geodjango.urls'

# Configurações de templates do Django
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Diretórios adicionais para buscar templates
        'APP_DIRS': True,  # Procura templates dentro das aplicações instaladas
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Configuração para aplicação WSGI
WSGI_APPLICATION = 'geodjango.wsgi.application'

# Configurações do banco de dados
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',  # Usando PostGIS para suporte GIS
        'NAME': 'conflitos',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Validação de senha para segurança
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Configurações de localização e fuso horário
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Configurações de arquivos estáticos e mídia
STATIC_URL = 'static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
STATIC_ROOT = BASE_DIR / 'static'

# Definição do tipo de campo padrão para chaves primárias
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configurações específicas para o Leaflet (biblioteca de mapas)
LEAFLET_CONFIG = {
    'DEFAULT_CENTER': (-22.77483256773132, -42.082277725096766),  # Centro padrão do mapa
    'DEFAULT_ZOOM': 10,  # Nível de zoom padrão
    'MAX_ZOOM': 20,  # Zoom máximo permitido
    'MIN_ZOOM': 3,  # Zoom mínimo permitido
    'SCALE': 'both',  # Mostrar escala no mapa
    'RESET_VIEW': False,  # Não redefinir a visualização ao adicionar camadas
}

# Configuração do CKEditor 5 com uma paleta de cores personalizada
customColorPalette = [
    {"color": "hsl(4, 90%, 58%)", "label": "Red"},
    {"color": "hsl(340, 82%, 52%)", "label": "Pink"},
    {"color": "hsl(291, 64%, 42%)", "label": "Purple"},
    {"color": "hsl(262, 52%, 47%)", "label": "Deep Purple"},
    {"color": "hsl(231, 48%, 48%)", "label": "Indigo"},
    {"color": "hsl(207, 90%, 54%)", "label": "Blue"},
]

# Configurações do CKEditor 5
CKEDITOR_5_CONFIGS = {
    # Configuração padrão do CKEditor
    "default": {
        "toolbar": [
            "heading",
            "|",
            "bold",
            "italic",
            "link",
            "bulletedList",
            "numberedList",
            "blockQuote",
            "imageUpload"
        ],
    },
    # Configuração de comentários para o CKEditor
    "comment": {
        "language": {"ui": "en", "content": "en"},
        "toolbar": [
            "heading",
            "|",
            "bold",
            "italic",
            "link",
            "bulletedList",
            "numberedList",
            "blockQuote",
        ],
    },
    # Configuração estendida do CKEditor
    "extends": {
        "language": "en",
        "blockToolbar": [
            "paragraph",
            "heading1",
            "heading2",
            "heading3",
            "|",
            "bulletedList",
            "numberedList",
            "|",
            "blockQuote",
        ],
        "toolbar": [
            "heading",
            "codeBlock",
            "|",
            "outdent",
            "indent",
            "|",
            "bold",
            "italic",
            "link",
            "underline",
            "strikethrough",
            "code",
            "subscript",
            "superscript",
            "highlight",
            "|",
            "bulletedList",
            "numberedList",
            "todoList",
            "|",
            "blockQuote",
            "insertImage",
            "|",
            "fontSize",
            "fontFamily",
            "fontColor",
            "fontBackgroundColor",
            "mediaEmbed",
            "removeFormat",
            "insertTable",
            "sourceEditing",
        ],
        "image": {
            "toolbar": [
                "imageTextAlternative",
                "|",
                "imageStyle:alignLeft",
                "imageStyle:alignRight",
                "imageStyle:alignCenter",
                "imageStyle:side",
                "|",
                "toggleImageCaption",
                "|"
            ],
            "styles": [
                "full",
                "side",
                "alignLeft",
                "alignRight",
                "alignCenter",
            ],
        },
        "table": {
            "contentToolbar": [
                "tableColumn",
                "tableRow",
                "mergeTableCells",
                "tableProperties",
                "tableCellProperties",
            ],
            "tableProperties": {
                "borderColors": customColorPalette,
                "backgroundColors": customColorPalette,
            },
            "tableCellProperties": {
                "borderColors": customColorPalette,
                "backgroundColors": customColorPalette,
            },
        },
        "heading": {
            "options": [
                {
                    "model": "paragraph",
                    "title": "Paragraph",
                    "class": "ck-heading_paragraph",
                },
                {
                    "model": "heading1",
                    "view": "h1",
                    "title": "Heading 1",
                    "class": "ck-heading_heading1",
                },
                {
                    "model": "heading2",
                    "view": "h2",
                    "title": "Heading 2",
                    "class": "ck-heading_heading2",
                },
                {
                    "model": "heading3",
                    "view": "h3",
                    "title": "Heading 3",
                    "class": "ck-heading_heading3",
                },
            ]
        },
        "htmlSupport": {
            "allow": [
                {
                    "name": "/.*/",
                    "attributes": True,
                    "classes": True,
                    "styles": True,
                }
            ]
        },
    },
}

# Configuração de backend de mensagens do Django para integração com o Crispy Forms
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

JAZZMIN_SETTINGS = {
    # Títulos e logos
    "site_title": "Administração Conflitos Ambientais",
    "site_header": "Conflitos Ambientais",
    "site_brand": "Admin - ConflitosAmb",
    "site_logo": "assets/Logo.svg",  # Atualize para o caminho correto do logo
    "login_logo": "assets/Pin.png",
    "site_icon": "assets/Logo.svg",  # Atualize para o caminho correto do favicon
    "welcome_sign": "Bem-vindo à administração de Conflitos Ambientais",
    "copyright": "© 2024 IFRJ",
    "search_model": ["posts.Post", "markers.Marker"],

    # Avatar do usuário
    "user_avatar": None,

    # Links do menu superior
    "topmenu_links": [
        {"name": "Início", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "Visualizar o site", "url": "markers:markersmapview", "new_window": True},
        {"model": "auth.User"},
        {"app": "posts"},
        {"app": "markers"},

    ],

    # Links do menu do usuário
    "usermenu_links": [
        {"name": "Perfil", "url": "admin:auth_user_change", "permissions": ["auth.change_user"]},
    ],

    # Menu lateral
    "show_sidebar": True,
    "navigation_expanded": False,
    "hide_apps": [],
    "hide_models": [],
    "order_with_respect_to": ["auth", "posts", "markers", "sobre", "tipografia"],
    "custom_links": {
        "posts": [{
            "name": "Adicionar Post",
            "url": "admin:posts_post_add",
            "icon": "fas fa-plus-circle",
            "permissions": ["posts.add_post"]
        }],
        "markers": [
            {
                "name": "Adicionar Marcador",
                "url": "admin:markers_marker_add",  # URL para adicionar um novo marcador
                "icon": "fas fa-map-marker-alt",
                "permissions": ["markers.add_marker"],  # Permissão para adicionar marcador
            },
        ],
    },

    # Ícones personalizados
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "posts": "fas fa-newspaper",
        "posts.Post": "fas fa-file-alt",
        "markers": "fas fa-map-marker-alt",
        "sobre": "fas fa-info-circle",
        "tipografia": "fas fa-font",
        "tipografia.Conflito": "fas fa-exclamation-triangle",
    },
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

    # Modal relacionado
    "related_modal_active": True,

    # Ajustes de UI
    "use_google_fonts_cdn": True,
    "show_ui_builder": False,

    # Formato da view de mudança
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"},
}
