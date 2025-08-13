from flask import Flask, request, render_template, redirect, url_for
 
dist = {
    'bagalkote':{
        'name': 'Bagalkote',
        'image_path': 'images/bagalkote.webp',
        'description': 'Bagalkote is known for its rich history and cultural heritage. The district is home to the famous Badami cave temples, Aihole, and Pattadakal, which are UNESCO World Heritage Sites. It is renowned for its contribution to music and literature in Karnataka. The Krishna River flows through the region, supporting agriculture and providing scenic beauty. Bagalkote is also famous for its vibrant festivals, traditional crafts, and a blend of ancient and modern lifestyles, making it a unique destination for tourists and historians alike.'
    },
    'bengaluru urban':{
        'name': 'Bangalore',
        'image_path': 'images/bengaluru_urban.webp',
        'description': 'Bangalore, the capital city of Karnataka, is known as the Silicon Valley of India. It is a major hub for information technology, startups, and innovation. The city boasts a pleasant climate, beautiful gardens like Lalbagh and Cubbon Park, and a cosmopolitan culture with diverse cuisine and nightlife. Bangalore is also home to prestigious educational and research institutions, vibrant art and music scenes, and a rich history reflected in its palaces and temples. Its rapid growth and modern infrastructure attract people from all over the country.'
    },
    'bengaluru rural':{
        'name': 'Bangalore Rural',
        'image_path': 'images/bengaluru_rural.webp',
        'description': 'Bangalore Rural is known for its agricultural richness and scenic landscapes. The district is dotted with vineyards, silk farms, and ancient temples. It serves as a green belt for the city and is famous for its rural tourism, trekking spots, and traditional village life. The region supports horticulture and floriculture, supplying produce to Bangalore city. Bangalore Rural offers a peaceful environment, blending natural beauty with cultural heritage, and is an emerging destination for eco-tourism and adventure activities.'
    },
    'belagavi':{
        'name': 'Belagavi',
        'image_path': 'images/belagavi.webp',
        'description': 'Belagavi is famous for its historical forts and temples. It is a major educational and commercial center in North Karnataka. The district is known for its sugarcane fields, rich cultural heritage, and the annual Kittur Utsav celebrating the legacy of Rani Chennamma. Belagavi’s strategic location near the borders of Maharashtra and Goa adds to its cultural diversity. The city is also an important military center and is surrounded by lush greenery, waterfalls, and hill stations, making it a popular tourist destination.'
    },
    'bellary':{
        'name': 'Bellary',
        'image_path': 'images/ballary.webp',
        'description': 'Bellary, located in the eastern part of Karnataka, is renowned for its rich mineral resources, especially iron ore, which has contributed significantly to the region’s economy. The district is steeped in history, with ancient forts such as the Bellary Fort and numerous temples reflecting its cultural heritage. Bellary is also known for its vibrant markets and traditional crafts. The Tungabhadra River flows through the district, supporting agriculture and providing scenic beauty. The region has witnessed rapid industrial growth, yet it retains its historical charm, making it a unique blend of the old and the new.'
    },
    'bidar':{
        'name': 'Bidar',
        'image_path': 'images/bidar.jpeg',
        'description': 'Bidar, situated in the northern tip of Karnataka, is famous for its unique Bidriware handicrafts and impressive historical monuments. The city is home to the majestic Bidar Fort, ancient mosques, and beautiful tombs that showcase Indo-Islamic architecture. Bidar has a rich cultural legacy, with influences from various dynasties that ruled the region. The district is also known for its educational institutions and vibrant festivals. Its strategic location and historical significance make Bidar a prominent destination for history enthusiasts and tourists alike.'
    },
    'bijapur':{
        'name': 'Bijapur',
        'image_path': 'images/bijapura.jpeg',
        'description': 'Bijapur, now officially known as Vijayapura, is celebrated for its grand historical monuments, including the iconic Gol Gumbaz with its remarkable whispering gallery. The city was once the capital of the Adil Shahi dynasty, and its landscape is dotted with impressive mosques, palaces, and mausoleums. Bijapur’s rich architectural heritage reflects a blend of Persian, Turkish, and Indian styles. The district is also known for its vibrant culture, traditional music, and delicious cuisine, making it a fascinating destination for visitors interested in history and art.'
    },
    'chamarajanagara':{
        'name': 'Chamarajanagara',
        'image_path': 'images/Chamarajanagara.webp',
        'description': 'Chamarajanagara, located in the southernmost part of Karnataka, is renowned for its natural beauty and abundant wildlife. The district is home to several wildlife sanctuaries and national parks, including Bandipur and Biligiri Rangaswamy Temple (BRT) Tiger Reserve. Chamarajanagara is also known for its ancient temples and vibrant tribal culture. The region’s lush forests, rolling hills, and rich biodiversity make it a haven for nature lovers and adventure seekers. Agriculture and sericulture are major occupations, contributing to the district’s rural charm.'
    },
    'chikkaballapura':{
        'name': 'Chikkaballapura',
        'image_path': 'images/Chikkaballapura.webp',
        'description': 'Chikkaballapura is famous for its picturesque hills, historical temples, and pleasant climate. Located close to Bengaluru, the district is a popular weekend getaway for trekking and nature enthusiasts. Nandi Hills, a well-known hill station, is a major attraction here. The region is also noted for its grape and silk production, contributing to the local economy. Chikkaballapura’s blend of natural beauty, cultural heritage, and agricultural prosperity makes it a unique and inviting destination in Karnataka.'
    },
    'chikkamagaluru':{
        'name': 'Chikkamagaluru',
        'image_path': 'images/Chikmagalur.webp',
        'description': 'Chikkamagaluru, often called the coffee land of Karnataka, is renowned for its sprawling coffee plantations and scenic hills. The district is nestled in the Western Ghats and offers breathtaking views, lush forests, and pleasant weather. It is a popular destination for trekking, wildlife spotting, and exploring ancient temples. Chikkamagaluru’s rich biodiversity, vibrant culture, and warm hospitality attract tourists from across the country, making it a must-visit for nature lovers and adventure seekers.'
    },
    'chitradurga':{
        'name': 'Chitradurga',
        'image_path': 'images/Chitradurga.webp',
        'description': 'Chitradurga is famous for its massive fort, which stands as a testament to the region’s historical significance and architectural brilliance. The district is dotted with ancient temples, rock formations, and picturesque landscapes. Chitradurga has a rich folklore tradition and is known for its vibrant festivals and cultural events. The region’s semi-arid climate supports agriculture, with crops like groundnut and sunflower being prominent. Chitradurga’s blend of history, culture, and natural beauty makes it a fascinating destination.'
    },
    'dakshina kannada':{
        'name': 'Dakshina Kannada',
        'image_path': 'images/Dakshin_ Kannada.webp',
        'description': 'Dakshina Kannada, located along the Arabian Sea coast, is known for its pristine beaches, lush greenery, and diverse culture. The district is a major educational and commercial hub, with Mangaluru as its headquarters. Dakshina Kannada is famous for its temples, churches, and mosques, reflecting a harmonious blend of traditions. The region’s cuisine, especially seafood, is widely celebrated. With its scenic beauty, vibrant festivals, and thriving industries, Dakshina Kannada is a dynamic and attractive district in Karnataka.'
    },
    'davanagere':{
        'name': 'Davanagere',
        'image_path': 'images/Davanagere.webp',
        'description': 'Davanagere, situated in the heart of Karnataka, is renowned for its unique cuisine, especially the famous Davanagere Benne Dosa. The district is a major educational center, with several prominent institutions. Davanagere’s economy is driven by agriculture and textile industries. The region is also known for its cultural events, historical sites, and friendly people. Its central location makes it an important commercial and transportation hub, connecting various parts of the state.'
    },
    'dharwad':{
        'name': 'Dharwad',
        'image_path': 'images/Dharwad.webp',
        'description': 'Dharwad, along with its twin city Hubballi, is known for its educational institutions, classical music, and cultural heritage. The district has produced many renowned musicians, writers, and artists. Dharwad’s pleasant climate, green surroundings, and historical landmarks make it a charming place to visit. The region is also famous for its unique Dharwad peda, a popular sweet. With its blend of tradition and modernity, Dharwad is a significant cultural center in Karnataka.'
    },
    'gadag':{
        'name': 'Gadag',
        'image_path': 'images/Gadag.png',
        'description': 'Gadag is known for its ancient temples, rich cultural heritage, and contributions to Kannada literature. The district is home to the famous Trikuteshwara Temple and several other architectural marvels. Gadag has a vibrant tradition of folk arts and music. Agriculture is the mainstay of the local economy, with crops like cotton and groundnut being widely cultivated. The district’s historical significance and cultural vibrancy make it an interesting destination for visitors.'
    },
    'hassan':{
        'name': 'Hassan',
        'image_path': 'images/Hassan.webp',
        'description': 'Hassan is famous for its historical sites, beautiful landscapes, and ancient temples. The district is home to the renowned Hoysala temples of Belur and Halebidu, which are UNESCO World Heritage Sites. Hassan’s pleasant climate, lush coffee plantations, and scenic hills attract tourists throughout the year. The region’s rich history, architectural wonders, and natural beauty make it a must-visit destination in Karnataka.'
    },
    'haveri':{
        'name': 'Haveri',
        'image_path': 'images/Haveri.webp',
        'description': 'Haveri is known for its agricultural richness, historical significance, and ancient temples. The district is a major producer of cotton, chili, and oilseeds. Haveri’s cultural heritage is reflected in its traditional art forms, music, and festivals. The region is dotted with beautiful lakes and green fields, offering a serene rural landscape. Haveri’s blend of history, culture, and agriculture makes it an important district in Karnataka.'
    },
    'kalaburagi':{
        'name': 'Kalaburagi',
        'image_path': 'images/Gulbarga.png',
        'description': 'Kalaburagi, formerly known as Gulbarga, is famous for its historical monuments, vibrant culture, and unique cuisine. The district is home to the magnificent Gulbarga Fort, ancient mosques, and dargahs. Kalaburagi is also known for its toor dal (pigeon pea) production, which is a staple in Indian kitchens. The region’s rich history, architectural marvels, and cultural diversity make it a fascinating place to explore.'
    },
    'kodagu':{
        'name': 'Kodagu',
        'image_path': 'images/Kodagu.webp',
        'description': 'Kodagu, also known as Coorg, is renowned for its lush greenery, coffee plantations, and misty hills. The district is a popular tourist destination, offering opportunities for trekking, river rafting, and wildlife spotting. Kodagu’s unique culture, traditional festivals, and delicious cuisine add to its charm. The region’s scenic beauty, pleasant climate, and warm hospitality make it a favorite getaway for nature lovers and adventure enthusiasts.'
    },
    'kolar':{
        'name': 'Kolar',
        'image_path': 'images/Kolar.webp',
        'description': 'Kolar is famous for its ancient gold mines, historical temples, and scenic landscapes. The district has a rich history, with several dynasties leaving their mark on its architecture and culture. Kolar is also known for its silk production and vibrant markets. The region’s blend of history, spirituality, and natural beauty makes it an interesting destination for visitors seeking a unique experience in Karnataka.'
    },
    'koppal':{
        'name': 'Koppal',
        'image_path': 'images/Koppal.webp',
        'description': 'Koppal, located in the northern part of Karnataka, is known for its rich history and archaeological sites. The district is home to ancient temples, forts, and inscriptions that reflect its glorious past. Koppal is also famous for the Mahadeva Temple at Itagi, considered one of the finest examples of Chalukyan architecture. Agriculture is the mainstay of the local economy, with crops like paddy, cotton, and pulses being widely cultivated. The region’s vibrant festivals, traditional crafts, and scenic landscapes make it an interesting destination for history buffs and travelers.'
    },
    'mandya':{
        'name': 'Mandya',
        'image_path': 'images/Mandya.webp',
        'description': 'Mandya, often referred to as the "Sugar Bowl of Karnataka," is renowned for its vast sugarcane fields and thriving agricultural sector. The district is irrigated by the Cauvery River, which supports the cultivation of sugarcane, paddy, and other crops. Mandya is also known for its rich cultural heritage, with several ancient temples and historical sites. The region’s vibrant festivals, traditional music, and folk arts add to its charm. Mandya’s scenic beauty, coupled with its agricultural prosperity, makes it a vital district in Karnataka.'
    },
    'mysuru':{
        'name': 'Mysuru',
        'image_path': 'images/Mysore.webp',
        'description': 'Mysuru, formerly known as Mysore, is celebrated for its royal heritage, magnificent palaces, and grand Dasara festival. The city is home to the iconic Mysore Palace, Chamundi Hill, and several museums and art galleries. Mysuru is also known for its silk, sandalwood, and traditional sweets like Mysore Pak. The district’s rich cultural legacy, vibrant markets, and beautiful gardens attract tourists from across the globe. Mysuru’s blend of history, culture, and modernity makes it one of the most popular destinations in Karnataka.'
    },
    'raichur':{
        'name': 'Raichur',
        'image_path': 'images/Raichur.webp',
        'description': 'Raichur, situated between the Krishna and Tungabhadra rivers, is known for its historical forts, ancient temples, and rich agricultural lands. The Raichur Fort, with its impressive architecture, stands as a testament to the region’s strategic importance in history. The district is a major producer of paddy, cotton, and oilseeds. Raichur’s diverse culture, traditional crafts, and vibrant festivals reflect its unique heritage. The region’s scenic beauty, coupled with its historical significance, makes Raichur an intriguing place to visit.'
    },
    'ramanagara':{
        'name': 'Ramanagara',
        'image_path': 'images/Ramanagara.webp',
        'description': 'Ramanagara, often called the "Silk City," is famous for its thriving silk industry and picturesque landscapes. The district is dotted with rocky hills and is a popular destination for trekking and rock climbing. Ramanagara’s silk cocoon market is one of the largest in Asia. The region is also known for its role in the iconic Bollywood movie "Sholay." With its blend of natural beauty, adventure activities, and cultural heritage, Ramanagara attracts tourists and nature enthusiasts alike.'
    },
    'shivamogga':{
        'name': 'Shivamogga',
        'image_path': 'images/Shimoga.webp',
        'description': 'Shivamogga, often referred to as the "Gateway to the Western Ghats," is known for its lush greenery, waterfalls, and rich biodiversity. The district is home to the famous Jog Falls, one of the highest waterfalls in India. Shivamogga’s fertile lands support the cultivation of arecanut, paddy, and spices. The region’s vibrant culture, historical temples, and wildlife sanctuaries make it a haven for nature lovers and adventure seekers. Shivamogga’s scenic beauty and cultural richness make it a must-visit destination in Karnataka.'
    },
    'tumakuru':{
        'name': 'Tumakuru',
        'image_path': 'images/Tumakuru.webp',
        'description': 'Tumakuru, located near Bengaluru, is known for its educational institutions, industrial growth, and agricultural prosperity. The district is a major producer of coconuts, groundnuts, and millets. Tumakuru is also famous for its scenic hills, such as Devarayanadurga and Shivagange, which are popular trekking spots. The region’s rich history is reflected in its ancient temples and forts. Tumakuru’s blend of tradition, modernity, and natural beauty makes it an important district in Karnataka.'
    },
    'udupi':{
        'name': 'Udupi',
        'image_path': 'images/Udupi.webp',
        'description': 'Udupi, located on the southwestern coast of Karnataka, is renowned for its ancient Krishna temple, pristine beaches, and unique cuisine. The district is a major center of pilgrimage and is famous for its traditional Udupi cuisine, especially vegetarian dishes. Udupi’s scenic coastline, vibrant festivals, and cultural heritage attract tourists and devotees from all over the country. The region’s blend of spirituality, natural beauty, and culinary delights makes Udupi a cherished destination.'
    },
    'uttara kannada':{
        'name': 'Uttara Kannada',
        'image_path': 'images/Uttara_Kannada.webp',
        'description': 'Uttara Kannada, stretching along the Arabian Sea, is famous for its stunning beaches, dense forests, and diverse wildlife. The district is home to several national parks and wildlife sanctuaries, including Anshi and Dandeli. Uttara Kannada’s rich cultural heritage is reflected in its temples, folk arts, and festivals. The region’s economy is driven by agriculture, forestry, and fishing. With its breathtaking landscapes, adventure opportunities, and cultural vibrancy, Uttara Kannada is a paradise for nature lovers and explorers.'
    },
    'yadgir':{
        'name': 'Yadgir',
        'image_path': 'images/Yadgir.webp',
        'description': 'Yadgir, located in the northeastern part of Karnataka, is known for its historical significance, ancient forts, and agricultural practices. The district is a major producer of paddy, pulses, and oilseeds. Yadgir’s landscape is dotted with hills, rivers, and reservoirs, adding to its natural charm. The region’s rich history is evident in its forts and temples, while its vibrant culture is showcased through local festivals and traditions. Yadgir’s blend of history, agriculture, and scenic beauty makes it a unique district in Karnataka.'
    }
 }

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    if request.method == 'POST':
        selected_dist=request.form['dist']
        return redirect(url_for('show_dist', selected_dist=selected_dist))
    return render_template('index.html',dist=dist)
    
@app.route('/dist/<selected_dist>')
def show_dist(selected_dist):
    if selected_dist not in dist:
        return "District not found", 404
    return render_template('dist_page.html', sel_dist=dist[selected_dist])
    
if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)