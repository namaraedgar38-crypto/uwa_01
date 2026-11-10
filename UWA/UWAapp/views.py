from django.http import Http404
from django.shortcuts import render


PARKS = [
    {
        'slug': 'bwindi-impenetrable',
        'name': 'Bwindi Impenetrable',
        'type': 'Gorilla trekking',
        'location': 'South-western Uganda',
        'image': 'photo-1516026672322-bc52d61a55d5',
        'summary': 'A remarkable forest landscape and home to the endangered mountain gorilla.',
        'description': 'Ancient rainforest, misty ridgelines and rich biodiversity make Bwindi one of Uganda’s most unforgettable protected areas. Gorilla trekking is managed through permits and guided visits.',
        'highlights': ['Mountain gorilla trekking', 'Guided forest walks', 'Birding and community experiences'],
    },
    {
        'slug': 'queen-elizabeth',
        'name': 'Queen Elizabeth',
        'type': 'Savannah & wildlife',
        'location': 'Western Uganda',
        'image': 'photo-1549366021-9f761d450615',
        'summary': 'Open savannah, crater lakes and the wildlife-rich Kazinga Channel.',
        'description': 'A varied landscape of grassland, wetlands, lakes and forest gives Queen Elizabeth National Park exceptional wildlife and birdlife. Explore with a qualified guide and follow park guidance.',
        'highlights': ['Kazinga Channel boat trips', 'Game drives', 'Crater lakes and scenic viewpoints'],
    },
    {
        'slug': 'murchison-falls',
        'name': 'Murchison Falls',
        'type': 'Waterfalls & safari',
        'location': 'North-western Uganda',
        'image': 'photo-1516426122078-c23e76319801',
        'summary': 'The Nile squeezes through a narrow gorge before continuing through open country.',
        'description': 'Murchison Falls National Park brings together the Nile, dramatic falls and broad savannah. Boat trips and guided game drives offer different ways to experience this diverse landscape.',
        'highlights': ['Murchison Falls viewpoints', 'Nile boat trips', 'Guided savannah game drives'],
    },
    {
        'slug': 'kibale',
        'name': 'Kibale Forest',
        'type': 'Forest & primates',
        'location': 'Western Uganda',
        'image': 'photo-1448375240586-882707db888b',
        'summary': 'A lush tropical forest known for guided chimpanzee tracking.',
        'description': 'Kibale’s tropical forest supports a diverse community of primates and other wildlife. Visitors can join guided forest experiences and learn about the importance of protecting forest habitats.',
        'highlights': ['Guided chimpanzee tracking', 'Forest nature walks', 'Birdwatching'],
    },
    {
        'slug': 'kidepo-valley',
        'name': 'Kidepo Valley',
        'type': 'Remote wilderness',
        'location': 'North-eastern Uganda',
        'image': 'photo-1518837695005-2083093ee35b',
        'summary': 'A remote wilderness of rugged mountains, open plains and wide skies.',
        'description': 'Set among the landscapes of north-eastern Uganda, Kidepo Valley offers a quieter wilderness experience. Plan ahead for travel and check current access and park information before setting out.',
        'highlights': ['Guided wildlife viewing', 'Narus Valley landscapes', 'Cultural experiences nearby'],
    },
    {
        'slug': 'lake-mburo',
        'name': 'Lake Mburo',
        'type': 'Lakeside safari',
        'location': 'Western Uganda',
        'image': 'photo-1472396961693-142e6e269027',
        'summary': 'Rolling acacia woodland and lakeside scenery in a compact park.',
        'description': 'Lake Mburo National Park protects a mosaic of grassland, woodland and wetlands. Guided activities provide a closer look at its landscapes and wildlife.',
        'highlights': ['Guided nature walks', 'Boat trips on Lake Mburo', 'Game drives'],
    },
]

PAGES = {
    'about': {
        'eyebrow': 'Who we are',
        'title': 'Wildlife belongs to all of us.',
        'intro': 'Uganda Wildlife Authority works to conserve Uganda’s wildlife and protected areas, for the benefit of people and nature.',
        'sections': [
            {'title': 'Our work', 'text': 'We protect wildlife and the habitats they depend on, support responsible tourism and work alongside communities who live near protected areas.'},
            {'title': 'Our purpose', 'text': 'Healthy ecosystems sustain wildlife, strengthen local livelihoods and preserve Uganda’s natural heritage for future generations.'},
            {'title': 'Working together', 'text': 'Conservation is a shared effort. Visitors, communities, conservation partners and public institutions all have a role to play.'},
        ],
        'cta': 'Explore Uganda’s parks',
        'cta_url': 'destinations',
    },
    'conservation': {
        'eyebrow': 'Protecting what matters',
        'title': 'A future where wildlife thrives.',
        'intro': 'Conservation connects protected landscapes, wildlife and the people who call these places home.',
        'sections': [
            {'title': 'Protecting habitats', 'text': 'Safeguarding forests, wetlands and savannah helps wildlife move, feed and flourish. Responsible land and resource use strengthens these natural systems.'},
            {'title': 'Living alongside wildlife', 'text': 'Community partnerships and practical coexistence approaches are essential to reducing conflict and building lasting support for conservation.'},
            {'title': 'Responsible tourism', 'text': 'Thoughtful travel helps visitors experience nature while respecting wildlife, local communities and the places they come to see.'},
        ],
        'cta': 'Plan a responsible visit',
        'cta_url': 'plan',
    },
    'plan': {
        'eyebrow': 'Make it meaningful',
        'title': 'Your visit can make a difference.',
        'intro': 'A little preparation helps protect wildlife and makes your time in Uganda’s wild places more rewarding.',
        'sections': [
            {'title': 'Before you travel', 'text': 'Check current park access, activity availability, fees, permit requirements and travel conditions through Uganda Wildlife Authority’s official channels before booking.'},
            {'title': 'Choose responsible experiences', 'text': 'Book guided activities through authorized providers, respect wildlife viewing distances and follow your guide and ranger’s instructions.'},
            {'title': 'Leave no trace', 'text': 'Take litter with you, stay on designated routes, keep noise low and never feed, touch or approach wild animals.'},
        ],
        'cta': 'Discover destinations',
        'cta_url': 'destinations',
    },
}


def home(request):
    return render(request, 'UWAapp/home.html', {'parks': PARKS[:3]})


def page(request, slug):
    content = PAGES.get(slug)
    if content is None:
        raise Http404('Page not found')
    return render(request, 'UWAapp/page.html', {'page': content})


def destinations(request):
    return render(request, 'UWAapp/destinations.html', {'parks': PARKS})


def destination_detail(request, slug):
    park = next((item for item in PARKS if item['slug'] == slug), None)
    if park is None:
        raise Http404('Destination not found')
    return render(request, 'UWAapp/destination_detail.html', {'park': park})


def contact(request):
    return render(request, 'UWAapp/contact.html')
