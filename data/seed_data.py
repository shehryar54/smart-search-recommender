import pandas as pd
import random
import json

random.seed(42)

CATEGORIES = {
    "video editing": {
        "tags": ["reels", "instagram", "youtube", "short-form", "transitions", "motion graphics", "color grading", "tiktok"],
        "titles": [
        "Instagram Reel Video Editor",
        "YouTube Video Editor & Colorist",
        "Short-Form Content Video Editor",
        "TikTok Video Editor with Effects",
        "Professional Video Editor for Social Media",
        "Motion Graphics & Video Editor",
    ]
}, 

    "graphic design": {
        "tags": ["logo", "branding", "poster", "flyer", "social media", "banner", "illustration", "ui design"],
        "titles": [
            "Professional Logo & Brand Designer",
            "Social Media Graphics Designer",
            "Flyer & Poster Designer",
            "Brand Identity Designer",
            "UI/UX Graphic Designer",
            "Illustration & Digital Art Designer",
        ]
    },

    "web development": {
    "tags": ["react", "nodejs", "fullstack", "frontend", "backend", "api", "html", "css", "javascript"],
    "titles": [
            "Full Stack Web Developer (React + Node)",
            "Frontend Developer - React Specialist",
            "Backend API Developer",
            "WordPress Website Developer",
            "E-commerce Web Developer",
            "JavaScript & Node.js Developer",
    ]
   },

    "content writing" : {
        "tags": ["blog", "seo", "copywriting", "articles", "product description", "social media", "ghostwriting"],
        "titles": [
            "SEO Blog Writer & Content Strategist",
            "Copywriter for Ads & Landing Pages",
            "Technical Content Writer",
            "Social Media Content Writer",
            "Product Description Writer",
            "Ghostwriter for Articles & Blogs",
        ]
    },

    "digital marketing": {
        "tags": ["seo", "social media", "facebook ads", "google ads", "email marketing", "influencer", "analytics"],
        "titles": [
            "Facebook & Instagram Ads Specialist",
            "SEO & Google Ads Expert",
            "Social Media Marketing Manager",
            "Email Marketing Specialist",
            "Digital Marketing Strategist",
            "Influencer Marketing Coordinator",
        ]
    },

    "mobile development": {
        "tags": ["flutter", "react native", "android", "ios", "firebase", "app development", "dart"],
        "titles": [
            "Flutter Mobile App Developer",
            "React Native App Developer",
            "Android App Developer (Kotlin)",
            "iOS App Developer (Swift)",
            "Cross-Platform Mobile Developer",
            "Firebase & Mobile Backend Developer",
        ]
    },

    "data science": {
        "tags": ["python", "machine learning", "data analysis", "visualization", "pandas", "tensorflow", "nlp"],
        "titles": [
            "Data Analyst & Visualization Expert",
            "Machine Learning Engineer",
            "NLP & AI Solutions Developer",
            "Python Data Scientist",
            "Business Intelligence Analyst",
            "Deep Learning & TensorFlow Specialist",

        ]
    },

    "photography": {
        "tags": ["portrait", "product", "wedding", "editing", "lightroom", "photoshop", "commercial"],
        "titles": [
            "Professional Portrait Photographer",
            "Product & E-commerce Photographer",
            "Wedding & Event Photographer",
            "Commercial Photography & Editing",
            "Photo Retouching Specialist",
            "Real Estate Photography Expert",
        ]
    },
    
    "voice over": {
        "tags": ["narration", "commercial", "podcast", "audiobook", "animation", "english", "dubbing"],
        "titles": [
            "Professional English Voice Over Artist",
            "Commercial & Ad Voice Over",
            "Audiobook Narrator",
            "Podcast Intro & Outro Voice Artist",
            "Animation Character Voice Over",
            "Corporate Narration Voice Artist",
        ]
    },

    "translation": {
        "tags": ["english", "arabic", "french", "urdu", "spanish", "document", "legal", "technical"],
        "titles": [
            "English to Arabic Translator",
            "Technical Document Translator",
            "Legal Translation Specialist",
            "English to Urdu Translator",
            "Spanish & English Translator",
            "Certified Document Translation",
        ]
    },
}

DESCRIPTIONS = {
    "video editing": "Experienced video editor specializing in {tags}. I deliver high-quality edits with smooth transitions, color grading, and engaging visuals tailored for {platform} audiences.",
    "graphic design": "Creative designer with expertise in {tags}. I craft visually compelling designs that communicate your brand message effectively across all platforms.",
    "web development": "Skilled developer proficient in {tags}. I build fast, responsive, and scalable web applications with clean code and modern best practices.",
    "content writing": "Professional writer specializing in {tags}. I create engaging, SEO-optimized content that drives traffic and converts readers into customers.",
    "digital marketing": "Results-driven marketer with hands-on experience in {tags}. I help businesses grow their online presence and maximize ROI through data-backed strategies.",
    "mobile development": "Mobile developer skilled in {tags}. I build smooth, user-friendly apps for both Android and iOS with clean architecture and great UX.",
    "data science": "Analytical professional with deep expertise in {tags}. I turn raw data into actionable insights and build intelligent models that solve real problems.",
    "photography": "Professional photographer with a keen eye for {tags}. I deliver stunning, high-resolution images with expert post-processing and attention to detail.",
    "voice over": "Versatile voice artist specializing in {tags}. I deliver clear, expressive recordings with professional studio-quality sound for any project.",
    "translation": "Certified translator fluent in {tags}. I provide accurate, culturally sensitive translations for documents, websites, and business communications."
}

def generate_description(category,tags):
    template = DESCRIPTIONS[category]
    tag_sample = ", ".join(random.sample(tags, min(3, len(tags))))
    platform = random.choice(["social media", "digital", "online", "modern"])
    return template.format(tags=tag_sample, platform=platform)  

def generate_dataset(num_entries=50):
    records = []
    categories = list(CATEGORIES.keys())

    
    entries_per_category = num_entries // len(categories)

    entry_id = 1
    for category in categories:
        titles = CATEGORIES[category]["titles"]
        tags_pool = CATEGORIES[category]["tags"]

        for i in range(entries_per_category):
            title = titles[i % len(titles)]
            selected_tags = random.sample(tags_pool, random.randint(3, 5))
            description = generate_description(category, selected_tags)
            rating = round(random.uniform(3.5, 5.0), 1)

            records.append({
                "id": entry_id,
                "title": title,
                "category": category,
                "tags": json.dumps(selected_tags),  
                "description": description,
                "rating": rating
            })
            entry_id += 1

    df = pd.DataFrame(records)
    df.to_csv("data/freelancers.csv", index=False)
    print(f"Dataset created: {len(df)} entries saved to data/freelancers.csv")
    print(f"\nCategory distribution:\n{df['category'].value_counts()}")
    print(f"\nSample entry:\n{df.iloc[0].to_dict()}")
    return df

if __name__ == "__main__":
    generate_dataset()