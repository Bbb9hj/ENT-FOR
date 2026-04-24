from flask import Flask, render_template, request

app = Flask(__name__)

# بيانات المحاضرات
lectures = [
    {
        "id": 1,
        "title": "Anatomy & physiology of ear",
        "doctor": "د.فؤاد شمسان",
        "category": "الأذن",
        "links": [
            {"label": "التقرير", "url": "https://t.me/september216thbatchENT/58", "type": "report"},
            {"label": "التسجيل", "url": "https://t.me/september216thbatchENT/56", "type": "recording"},
            {"label": "الملزمة", "url": "https://t.me/september216thbatchENT/55", "type": "handout"}
        ]
    },
    {
        "id": 2,
        "title": "Symptomatology & examination & Assessment of Ear",
        "doctor": "د.فؤاد شمسان",
        "category": "الأذن",
        "links": [
            {"label": "التقرير", "url": "https://t.me/september216thbatchENT/59", "type": "report"},
            {"label": "التسجيل", "url": "https://t.me/september216thbatchENT/57", "type": "recording"},
            {"label": "الملزمة", "url": "https://t.me/september216thbatchENT/55", "type": "handout"}
        ]
    },
    {
        "id": 3,
        "title": "Otosclerosis, Otitic Barotrauma and Facial nerve",
        "doctor": "د.حنان داؤود",
        "category": "الأذن",
        "links": [
            {"label": "التقرير", "url": "https://t.me/september216thbatchENT/75", "type": "report"},
            {"label": "التسجيل", "url": "https://t.me/september216thbatchENT/60", "type": "recording"},
            {"label": "الملزمة", "url": "https://t.me/september216thbatchENT/73", "type": "handout"}
        ]
    },
    {
        "id": 4,
        "title": "Diseases of Inner ear and Anatomy & Physiology of Nose & PNS",
        "doctor": "د.حنان داؤود",
        "category": "الأنف",
        "links": [
            {"label": "التقرير", "url": "https://t.me/september216thbatchENT/74", "type": "report"},
            {"label": "التسجيل", "url": "https://t.me/september216thbatchENT/62", "type": "recording"},
            {"label": "الملزمة", "url": "https://t.me/september216thbatchENT/73", "type": "handout"}
        ]
    },
    {
        "id": 5,
        "title": "Diseases of External Ear",
        "doctor": "د. ضياء السروري",
        "category": "الأذن",
        "links": [
            {"label": "التقرير", "url": "https://t.me/september216thbatchENT/77", "type": "report"},
            {"label": "التسجيل", "url": "https://t.me/september216thbatchENT/63", "type": "recording"},
            {"label": "الملزمة", "url": "https://t.me/september216thbatchENT/78", "type": "handout"}
        ]
    },
    {
        "id": 6,
        "title": "Acute Otitis media",
        "doctor": "د.زيد المراني",
        "category": "الأذن",
        "notes": "لا يوجد تسجيل، الدكتور منع التسجيل",
        "links": [
            {"label": "التقرير", "url": "https://t.me/september216thbatchENT/110", "type": "report"},
            {"label": "الملزمة", "url": "https://t.me/september216thbatchENT/101", "type": "handout"},
            {"label": "صور اضافية للملزمة", "url": "https://t.me/september216thbatchENT/109", "type": "extra"}
        ]
    },
    {
        "id": 7,
        "title": "Anatomy and physiology of the larynx",
        "doctor": "د.خالد عثرب",
        "category": "الحنجرة",
        "links": [
            {"label": "التقرير", "url": "https://t.me/september216thbatchENT/87", "type": "report"},
            {"label": "التسجيل", "url": "https://t.me/september216thbatchENT/79", "type": "recording"},
            {"label": "الملزمة", "url": "https://t.me/september216thbatchENT/83", "type": "handout"}
        ]
    },
    {
        "id": 8,
        "title": "Tracheostomy",
        "doctor": "د.خالد عثرب",
        "category": "الحنجرة",
        "links": [
            {"label": "التقرير", "url": "https://t.me/september216thbatchENT/88", "type": "report"},
            {"label": "التسجيل", "url": "https://t.me/september216thbatchENT/80", "type": "recording"},
            {"label": "الملزمة", "url": "https://t.me/september216thbatchENT/84", "type": "handout"},
            {"label": "تفريغات دفع سابقة", "url": "https://t.me/september216thbatchENT/85", "type": "extra"}
        ]
    },
    {
        "id": 9,
        "title": "Diseases of Larynx",
        "doctor": "د.سلوى الحمادي",
        "category": "الحنجرة",
        "links": [
            {"label": "التقرير", "url": "https://t.me/september216thbatchENT/89", "type": "report"},
            {"label": "تسجيل 1", "url": "https://t.me/september216thbatchENT/81", "type": "recording"},
            {"label": "تسجيل 2", "url": "https://t.me/september216thbatchENT/82", "type": "recording"},
            {"label": "الملزمة", "url": "https://t.me/september216thbatchENT/86", "type": "handout"}
        ]
    },
    {
        "id": 10,
        "title": "Rhinosinusitis",
        "doctor": "د.نجلاء المقالح",
        "category": "الأنف",
        "links": [
            {"label": "تقرير 1", "url": "https://t.me/september216thbatchENT/91", "type": "report"},
            {"label": "تقرير 2", "url": "https://t.me/september216thbatchENT/99", "type": "report"},
            {"label": "التسجيل", "url": "https://t.me/september216thbatchENT/90", "type": "recording"},
            {"label": "الملزمة", "url": "https://t.me/september216thbatchENT/98", "type": "handout"}
        ]
    },
    {
        "id": 11,
        "title": "Chronic Otitis media",
        "doctor": "د.زيد المراني",
        "category": "الأذن",
        "links": [
            {"label": "التقرير", "url": "https://t.me/september216thbatchENT/159", "type": "report"},
            {"label": "الملزمة", "url": "https://t.me/september216thbatchENT/151", "type": "handout"}
        ]
    },
    {
        "id": 12,
        "title": "Anatomy and physiology of oral cavity & pharynx",
        "doctor": "د.جديس الحكيمي",
        "category": "البلعوم",
        "links": [
            {"label": "التقرير", "url": "https://t.me/september216thbatchENT/122", "type": "report"},
            {"label": "الملزمة", "url": "https://t.me/september216thbatchENT/123", "type": "handout"}
        ]
    },
    {
        "id": 13,
        "title": "Adenoidotonsillar disease",
        "doctor": "د.جديس الحكيمي",
        "category": "البلعوم",
        "links": [
            {"label": "التسجيل", "url": "https://t.me/september216thbatchENT/138", "type": "recording"},
            {"label": "الملزمة", "url": "https://t.me/september216thbatchENT/140", "type": "handout"}
        ]
    },
    {
        "id": 14,
        "title": "Trauma and FB",
        "doctor": "د.خلدون الجبيلي",
        "category": "عام",
        "links": [
            {"label": "التقرير", "url": "https://t.me/september216thbatchENT/118", "type": "report"},
            {"label": "التسجيل", "url": "https://t.me/september216thbatchENT/117", "type": "recording"},
            {"label": "الملزمة", "url": "https://t.me/september216thbatchENT/119", "type": "handout"}
        ]
    },
    {
        "id": 15,
        "title": "Deep neck spaces infections and Update in ENT",
        "doctor": "د.سلوى الحمادي",
        "category": "الرقبة",
        "links": [
            {"label": "التقرير", "url": "https://t.me/september216thbatchENT/126", "type": "report"},
            {"label": "التسجيل", "url": "https://t.me/september216thbatchENT/124", "type": "recording"},
            {"label": "الملزمة", "url": "https://t.me/september216thbatchENT/125", "type": "handout"}
        ]
    },
    {
        "id": 16,
        "title": "DNS, Allergic & Rhinitis, Neck Mass & Tumors",
        "doctor": "د.خالد الطهيف",
        "category": "عام",
        "links": [
            {"label": "التقرير والتسجيل والملازم", "url": "https://t.me/september216thbatchENT/137", "type": "extra"}
        ]
    }
]

@app.route('/')
def index():
    return render_template('index.html', lectures=lectures)

if __name__ == '__main__':
    app.run(debug=True)