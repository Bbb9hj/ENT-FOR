from flask import Flask, render_template_string

app = Flask(__name__)

# بيانات المحاضرات
lectures = [
    {"id": 1, "title": "Anatomy & physiology of ear", "doctor": "د.فؤاد شمسان", "links": [{"label": "التقرير", "url": "https://t.me/september216thbatchENT/58"}, {"label": "التسجيل", "url": "https://t.me/september216thbatchENT/56"}, {"label": "الملزمة", "url": "https://t.me/september216thbatchENT/55"}]},
    {"id": 2, "title": "Symptomatology & examination & Assessment of Ear", "doctor": "د.فؤاد شمسان", "links": [{"label": "التقرير", "url": "https://t.me/september216thbatchENT/59"}, {"label": "التسجيل", "url": "https://t.me/september216thbatchENT/57"}, {"label": "الملزمة", "url": "https://t.me/september216thbatchENT/55"}]},
    {"id": 3, "title": "Otosclerosis, Otitic Barotrauma and Facial nerve", "doctor": "د.حنان داؤود", "links": [{"label": "التقرير", "url": "https://t.me/september216thbatchENT/75"}, {"label": "التسجيل", "url": "https://t.me/september216thbatchENT/60"}, {"label": "الملزمة", "url": "https://t.me/september216thbatchENT/73"}]},
    {"id": 4, "title": "Diseases of Inner ear and Anatomy & Physiology of Nose & PNS", "doctor": "د.حنان داؤود", "links": [{"label": "التقرير", "url": "https://t.me/september216thbatchENT/74"}, {"label": "التسجيل", "url": "https://t.me/september216thbatchENT/62"}, {"label": "الملزمة", "url": "https://t.me/september216thbatchENT/73"}]},
    {"id": 5, "title": "Diseases of External Ear", "doctor": "د. ضياء السروري", "links": [{"label": "التقرير", "url": "https://t.me/september216thbatchENT/77"}, {"label": "التسجيل", "url": "https://t.me/september216thbatchENT/63"}, {"label": "الملزمة", "url": "https://t.me/september216thbatchENT/78"}]},
    {"id": 6, "title": "Acute Otitis media", "doctor": "د.زيد المراني", "notes": "لا يوجد تسجيل، الدكتور منع التسجيل", "links": [{"label": "التقرير", "url": "https://t.me/september216thbatchENT/110"}, {"label": "الملزمة", "url": "https://t.me/september216thbatchENT/101"}, {"label": "صور اضافية للملزمة", "url": "https://t.me/september216thbatchENT/109"}]},
    {"id": 7, "title": "Anatomy and physiology of the larynx", "doctor": "د.خالد عثرب", "links": [{"label": "التقرير", "url": "https://t.me/september216thbatchENT/87"}, {"label": "التسجيل", "url": "https://t.me/september216thbatchENT/79"}, {"label": "الملزمة", "url": "https://t.me/september216thbatchENT/83"}]},
    {"id": 8, "title": "Tracheostomy", "doctor": "د.خالد عثرب", "links": [{"label": "التقرير", "url": "https://t.me/september216thbatchENT/88"}, {"label": "التسجيل", "url": "https://t.me/september216thbatchENT/80"}, {"label": "الملزمة", "url": "https://t.me/september216thbatchENT/84"}, {"label": "تفريغات سابقة", "url": "https://t.me/september216thbatchENT/85"}]},
    {"id": 9, "title": "Diseases of Larynx", "doctor": "د.سلوى الحمادي", "links": [{"label": "التقرير", "url": "https://t.me/september216thbatchENT/89"}, {"label": "تسجيل 1", "url": "https://t.me/september216thbatchENT/81"}, {"label": "تسجيل 2", "url": "https://t.me/september216thbatchENT/82"}, {"label": "الملزمة", "url": "https://t.me/september216thbatchENT/86"}]},
    {"id": 10, "title": "Rhinosinusitis", "doctor": "د.نجلاء المقالح", "links": [{"label": "تقرير 1", "url": "https://t.me/september216thbatchENT/91"}, {"label": "تقرير 2", "url": "https://t.me/september216thbatchENT/99"}, {"label": "التسجيل", "url": "https://t.me/september216thbatchENT/90"}, {"label": "الملزمة", "url": "https://t.me/september216thbatchENT/98"}]},
    {"id": 11, "title": "Chronic Otitis media", "doctor": "د.زيد المراني", "links": [{"label": "التقرير", "url": "https://t.me/september216thbatchENT/159"}, {"label": "الملزمة", "url": "https://t.me/september216thbatchENT/151"}]},
    {"id": 12, "title": "Anatomy and physiology of oral cavity & pharynx", "doctor": "د.جديس الحكيمي", "links": [{"label": "التقرير", "url": "https://t.me/september216thbatchENT/122"}, {"label": "الملزمة", "url": "https://t.me/september216thbatchENT/123"}]},
    {"id": 13, "title": "Adenoidotonsillar disease", "doctor": "د.جديس الحكيمي", "links": [{"label": "التسجيل", "url": "https://t.me/september216thbatchENT/138"}, {"label": "الملزمة", "url": "https://t.me/september216thbatchENT/140"}]},
    {"id": 14, "title": "Trauma and FB", "doctor": "د.خلدون الجبيلي", "links": [{"label": "التقرير", "url": "https://t.me/september216thbatchENT/118"}, {"label": "التسجيل", "url": "https://t.me/september216thbatchENT/117"}, {"label": "الملزمة", "url": "https://t.me/september216thbatchENT/119"}]},
    {"id": 15, "title": "Deep neck spaces infections and Update in ENT", "doctor": "د.سلوى الحمادي", "links": [{"label": "التقرير", "url": "https://t.me/september216thbatchENT/126"}, {"label": "التسجيل", "url": "https://t.me/september216thbatchENT/124"}, {"label": "الملزمة", "url": "https://t.me/september216thbatchENT/125"}]},
    {"id": 16, "title": "DNS, Allergic & non- allergic Rhinits, Neck Mass & ENT Tumors", "doctor": "د.خالد الطهيف", "links": [{"label": "الرابط الشامل", "url": "https://t.me/september216thbatchENT/137"}]}
]

# كود الواجهة (HTML/JS/Tailwind)
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ENT Index - Batch 6</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700&display=swap" rel="stylesheet">
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>
        body { font-family: 'Tajawal', sans-serif; background-color: #f8fafc; }
        .no-scrollbar::-webkit-scrollbar { display: none; }
    </style>
</head>
<body class="pb-10">
    <!-- Header -->
    <header class="bg-white border-b sticky top-0 z-30 shadow-sm pt-6 pb-4 px-4 text-center">
        <div class="bg-blue-600 text-white w-10 h-10 rounded-xl flex items-center justify-center mx-auto mb-3 shadow-lg">
            <i data-lucide="graduation-cap"></i>
        </div>
        <h1 class="text-xl font-bold text-gray-900">فهرس قسم الـ ENT</h1>
        <p class="text-gray-500 text-[10px] mt-1">التسجيلات، الملازم، والتقارير - الدفعة السادسة</p>
        
        <div class="max-w-sm mx-auto mt-4 px-4">
            <div class="relative">
                <input type="text" id="searchInput" placeholder="ابحث عن محاضرة أو دكتور..." 
                       class="w-full bg-gray-100 border border-gray-200 rounded-lg py-2 pr-10 pl-4 text-xs focus:ring-2 focus:ring-blue-500 focus:bg-white outline-none transition-all">
                <i data-lucide="search" class="absolute right-3.5 top-2.5 w-4 h-4 text-gray-400"></i>
            </div>
        </div>
    </header>

    <!-- Main Content -->
    <main class="max-w-4xl mx-auto px-4 mt-8">
        <div id="lecturesGrid" class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <!-- Lectures will be injected here -->
        </div>
    </main>

    <footer class="mt-16 text-center py-8 border-t bg-white">
        <p class="text-[9px] text-gray-400 font-bold tracking-widest uppercase mb-4">Developed for</p>
        <p class="text-sm font-bold text-gray-900">اللجنة العلمية للدفعة السادسة</p>
    </footer>

    <script>
        const lectures = {{ lectures|tojson }};
        const grid = document.getElementById('lecturesGrid');
        const searchInput = document.getElementById('searchInput');

        function renderLectures(data) {
            grid.innerHTML = data.map(l => `
                <div class="bg-white rounded-2xl border border-gray-100 p-5 shadow-sm hover:shadow-md transition-all">
                    <div class="flex justify-between mb-4">
                        <span class="w-7 h-7 bg-gray-50 rounded-full flex items-center justify-center text-[10px] font-bold text-gray-400 border">${l.id}</span>
                        <span class="text-[9px] bg-blue-50 text-blue-600 px-2 py-0.5 rounded-full font-bold uppercase border border-blue-100">ENT</span>
                    </div>
                    <h3 class="text-base font-bold text-gray-900 mb-1.5 leading-tight">${l.title}</h3>
                    <p class="text-gray-500 text-xs font-semibold mb-4">${l.doctor}</p>
                    ${l.notes ? `<div class="bg-red-50 text-red-600 text-[10px] p-2 rounded-lg mb-4 flex items-start gap-2 border border-red-100 italic"><span>⚠</span> ${l.notes}</div>` : ''}
                    <div class="space-y-1.5 mt-auto border-t pt-4">
                        ${l.links.map(link => `
                            <a href="${link.url}" target="_blank" class="flex items-center justify-between px-3 py-2 bg-gray-50 rounded-xl text-xs font-bold text-gray-600 hover:bg-blue-600 hover:text-white transition-all border border-gray-100">
                                <span>${link.label}</span>
                                <i data-lucide="external-link" class="w-3 h-3 opacity-50"></i>
                            </a>
                        `).join('')}
                    </div>
                </div>
            `).join('');
            lucide.createIcons();
        }

        searchInput.addEventListener('input', (e) => {
            const val = e.target.value.toLowerCase();
            const filtered = lectures.filter(l => l.title.toLowerCase().includes(val) || l.doctor.includes(val));
            renderLectures(filtered);
        });

        renderLectures(lectures);
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE, lectures=lectures)

if __name__ == '__main__':
    app.run()