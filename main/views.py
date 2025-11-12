from django.shortcuts import render
from django.http import Http404
from pathlib import Path
import re
import html
from django.utils.translation import gettext_lazy as _

# Structured services data (easy to search and render)
SERVICES = [

	{
		'title': _('Advisory and Planning'),
		'slug': 'advisory-and-planning',
		'description': _("""Expert guidance through feasibility studies,
business and investor advisory, urban and
regional planning, policy development, and
stakeholder engagement to support sustainable
growth and informed decision-making.""")
	},
	{
		'title': _('Architecture and Design'),
		'slug': 'Architecture-and-Design',
		'description': _("""Creating iconic, user-centric designs for commercial,
         institutional, residential, science and industry,
         and hospitality projects, including refurbishments,
       teaching and research spaces, and inclusive, accessible
       environments..""")
	},
	{
		'title': _('3D modeling and Visualization'),
		'slug': '3d-modeling-visualization',
		'description': _("""Delivering robust structural, mechanical, civil, and
        bridge engineering, with a focus on
        efficiency and resilience.""")
	},
	{
		'title': _('Urban Design & Masterplanning'),
		'slug': 'urban-design-masterplanning',
		'description': _("""Designing sustainable, smart cities, urban
        frameworks, and campus energy masterplans,
        integrating intelligent mobility.""")
	},
	{
	    'title': _('Sustainability & Environmental Solutions'),
		'slug': 'sustainability-environmental-solutions',
		'description': _('Guiding clients towards net-zero goals with ESG '
		'strategies, environmental consulting, nature-based solutions '
		'and certifications like EDGE.')
	},
  {
	    'title': _('Digital innovation and Experimental Design'),
	    'slug': 'digital-innovation-experimental-design',
	    'description': _('Utilizing BIM, digital twinning, and parametric design for'
	    ' creating lighting design, night-time design, and immersive experience design for '
	    'cultural, public, and event spaces, including major event overlay design.')
	},
	{
		'title': _('Interior and Landscape Design'),
		'slug': 'Interior-and-Landscape-Design',
		'description': _('Designing standout interiors and landscape to support'
		' the building taking into consideration sustainability,and saint'
		' gobain comfort goals.')
	},
	{
		'title': _('Project Management'),
		'slug': 'project-management',
		'description': _('Employing agile methodologies for client-centric project management, '
		'alongside innovative product design and sustainable material specification.')
	},
	{
		'title': _('Specialized Services'),
		'slug': 'specialized-services',
		'description': _('Offering expertise in specialized services such as retrofit, at scale, research, and organizational development to support diverse project needs.')
	}



]

# Structured projects data
PROJECTS = [
    {
        'title': _('Amadia'),
        'slug': 'Amadia',
        'description': _('Development of a retail showcase of a warehouse combined with restaurants.'),
        'location': _('Accra, Ghana'),
        'image': 'amadia.jpg'
    },
    {
        'title': _('Aseda Garden Estate'),
        'slug': 'aseda-garden-estate',
        'description': _('Luxury home featuring innovative architecture. A bespoke residence with modern amenities and green spaces.'),
        'location': _('Tema, Ghana'),
        'image': 'Aseda Garden Estate.jpg'
    },
    {
        'title': _('Beach House'),
        'slug': 'beach-house',
        'description': _('Seaside retreat with panoramic ocean views. A coastal property designed for relaxation and harmony with nature.'),
        'location': _('Kokrobite, Ghana'),
        'image': 'Beach House.jpg'
    },
    {
        'title': _('First love center'),
        'slug': 'first-love-center',
        'description': _('Developing multiple components, from Internal to the new tower block.'),
        'location': _('East Legon, Ghana'),
        'image': 'First love center.jpg'
    },
    {
        'title': _('Gardenia'),
        'slug': 'gardenia',
        'description': _('Commercial complex with modern retail spaces. A vibrant hub for shopping and entertainment in the city center.'),
        'location': _('Accra, Ghana'),
        'image': 'Gardenia.jpg'
    },
    {
        'title': _('NetZero House'),
        'slug': 'netzero-house',
        'description': _('Rustic retreat nestled in the hills. An eco-lodge offering tranquility and adventure experiences.'),
        'location': _('Akwapim Hills, Ghana'),
        'image': 'NetZero HOuse.jpg'
    },
    {
        'title': _('private residence tema'),
        'slug': 'private-residence-tema',
        'description': _('High-rise residential towers with city views. Luxury apartments featuring smart home technology and amenities.'),
        'location': _('Accra, Ghana'),
        'image': 'private residence tema.jpg'
    },
    {
        'title': _('The Exchange apartments'),
        'slug': 'the-exchange-apartments',
        'description': _('Exclusive villas along the riverbank. Private estates with lush gardens and waterfront access.'),
        'location': _('Volta Region, Ghana'),
        'image': 'The Exchange apartments.jpg'
    },
    {
        'title': _('Theatre'),
        'slug': 'theatre-tema',
        'description': _('Sustainable community living spaces. A green development promoting environmental consciousness.'),
        'location': _('Kumasi, Ghana'),
        'image': 'Theatre, tema.jpg'
    },
    {
        'title': _('TSC Commercial, Tema'),
        'slug': 'tsc-commercial-tema',
        'description': _('Luxury accommodation with cultural significance. A boutique hotel preserving local heritage and traditions.'),
        'location': _('Cape Coast, Ghana'),
        'image': 'TSC Commercial, Tema.jpg'
    },
    {
        'title': _('roof top'),
        'slug': 'roof-top',
        'description': _('Tech and startup incubation center. A modern facility fostering entrepreneurship and innovation.'),
        'location': _('Accra, Ghana'),
        'image': 'roof top.jpg'
    },
    {
        'title': _('Private Residence Ashongman'),
        'slug': 'private-residence-ashongman',
        'description': _('Spa and wellness retreat destination. A serene oasis for relaxation and rejuvenation.'),
        'location': _('Takoradi, Ghana'),
        'image': 'Private Residence Ashongman.jpg'
    }
]


def home(request):
	return render(request, 'main/index.html')


def about(request):
	return render(request, 'main/about.html')


def projects(request):
	query = request.GET.get('q', '').strip()
	if query:
		q = query.lower()
		filtered = [p for p in PROJECTS if q in p['title'].lower() or q in p['description'].lower() or q in p['location'].lower()]
	else:
		filtered = PROJECTS
	return render(request, 'main/projects.html', {'projects_list': filtered, 'query': query})


def insights(request):
	return render(request, 'main/insights.html')


def careers(request):
	return render(request, 'main/careers.html')


def contact(request):
	return render(request, 'main/contact.html')


def markets(request):
	return render(request, 'main/markets.html')


def news(request):
	return render(request, 'main/news.html')


def services(request):
	# Render the services page and optionally filter services by query
	query = request.GET.get('q', '').strip()
	if query:
		q = query.lower()
		filtered = [s for s in SERVICES if q in s['title'].lower() or q in s['description'].lower()]
	else:
		filtered = SERVICES
	return render(request, 'main/services.html', {'services_list': filtered, 'query': query})


def service_detail(request, slug):
	"""Render a dedicated page for a single service identified by slug."""
	svc = None
	for s in SERVICES:
		if s.get('slug') == slug:
			svc = s
			break
	if svc is None:
		raise Http404('Service not found')
	# You could add richer content per-service here later
	return render(request, 'main/service_detail.html', {'service': svc})


def project_detail(request, slug):
	"""Render a dedicated page for a single project identified by slug."""
	proj = None
	for p in PROJECTS:
		if p.get('slug') == slug:
			proj = p
			break
	if proj is None:
		raise Http404('Project not found')
	# You could add richer content per-project here later
	return render(request, 'main/project_detail.html', {'project': proj})


def search(request):
	"""Simple site-wide search that scans the app templates for the query.

	This is a lightweight fallback when you don't have models to search.
	It looks through `main/templates/main/*.html` and returns pages whose
	template source contains the query (case-insensitive).
	"""
	query = request.GET.get('q', '').strip()
	scope = request.GET.get('scope', '').strip().lower()
	results = []
	if query:
		q = query.lower()
		# If the search was scoped to services, parse the services template
		# and return section-level matches (headings and nearby text).
		if scope == 'services':
			templates_dir = Path(__file__).resolve().parent / 'templates' / 'main'
			path = templates_dir / 'services.html'
			if path.exists():
				try:
					text = path.read_text(encoding='utf-8')
				except Exception:
					text = ''
				# Find h2/h3 headings and their following block (until next heading)
				sections = []
				for m in re.finditer(r'<h([2-3])[^>]*>(.*?)</h\1>', text, re.IGNORECASE | re.DOTALL):
					title = re.sub(r'<[^>]+>', '', m.group(2)).strip()
					start = m.end()
					# find next heading
					next_m = re.search(r'<h[2-3][^>]*>', text[start:], re.IGNORECASE)
					end = start + (next_m.start() if next_m else min(3000, len(text)-start))
					body = re.sub(r'<[^>]+>', '', text[start:end]).strip()
					sections.append({'title': html.unescape(title), 'body': html.unescape(body)})
				# If no h2/h3 found, try tokens in the whole page
				if not sections:
					# fall back to splitting by paragraphs
					for m in re.finditer(r'<p[^>]*>(.*?)</p>', text, re.IGNORECASE | re.DOTALL):
						ptext = re.sub(r'<[^>]+>', '', m.group(1)).strip()
						if ptext:
							sections.append({'title': ptext[:60], 'body': ptext})
				# Search sections for query
				for s in sections:
					st = s['title'].lower() + '\n' + s['body'].lower()
					if q in st:
						# simple snippet around first occurrence
						idx = st.find(q)
						start = max(0, idx - 80)
						end = min(len(st), idx + 80)
						snippet = s['body'][start:end].strip() if s['body'] else ''
						# remove Django template tags
						snippet = re.sub(r'{%.*?%}', '', snippet, flags=re.DOTALL)
						snippet = re.sub(r'{{.*?}}', '', snippet, flags=re.DOTALL)
						# highlight the query
						snippet = re.sub(re.escape(q), lambda m: f'<mark>{m.group()}</mark>', snippet, flags=re.IGNORECASE)
						# create an anchor-like slug for per-section links
						slug = re.sub(r"[^a-z0-9]+", '-', s['title'].lower()).strip('-') or 'section'
						results.append({'title': s['title'], 'url': f'/services/#{slug}', 'snippet': snippet, 'source': 'Services'})
			# remove duplicates (by title)
			seen = set()
			unique = []
			for r in results:
				if r['title'] not in seen:
					seen.add(r['title'])
					unique.append(r)
			results = unique
			return render(request, 'main/search_results.html', {'query': query, 'results': results})

		# Search projects
		for proj in PROJECTS:
			# Convert translation proxy objects to strings
			title_str = str(proj['title'])
			desc_str = str(proj['description'])
			title_lower = title_str.lower()
			desc_lower = desc_str.lower()
			if q in title_lower or q in desc_lower:
				snippet = desc_str
				# highlight
				snippet = re.sub(re.escape(q), lambda m: f'<mark>{m.group()}</mark>', snippet, flags=re.IGNORECASE)
				results.append({
					'title': title_str,
					'url': f'/projects/{proj["slug"]}/',
					'snippet': snippet,
					'source': 'Projects',
					'score': 50 if q in title_lower else 40
				})

		templates_dir = Path(__file__).resolve().parent / 'templates' / 'main'
		if templates_dir.exists():
			for path in templates_dir.glob('*.html'):
				try:
					text = path.read_text(encoding='utf-8')
				except Exception:
					continue
				name = path.stem
				# Skip the home page and projects page as they are handled separately
				if name in ('index', 'projects'):
					continue
				lower = text.lower()
			templates_dir = Path(__file__).resolve().parent / 'templates' / 'main'
			path = templates_dir / 'services.html'
			if path.exists():
				try:
					text = path.read_text(encoding='utf-8')
				except Exception:
					text = ''
				# Find h2/h3 headings and their following block (until next heading)
				sections = []
				for m in re.finditer(r'<h([2-3])[^>]*>(.*?)</h\1>', text, re.IGNORECASE | re.DOTALL):
					title = re.sub(r'<[^>]+>', '', m.group(2)).strip()
					start = m.end()
					# find next heading
					next_m = re.search(r'<h[2-3][^>]*>', text[start:], re.IGNORECASE)
					end = start + (next_m.start() if next_m else min(3000, len(text)-start))
					body = re.sub(r'<[^>]+>', '', text[start:end]).strip()
					sections.append({'title': html.unescape(title), 'body': html.unescape(body)})
				# If no h2/h3 found, try tokens in the whole page
				if not sections:
					# fall back to splitting by paragraphs
					for m in re.finditer(r'<p[^>]*>(.*?)</p>', text, re.IGNORECASE | re.DOTALL):
						ptext = re.sub(r'<[^>]+>', '', m.group(1)).strip()
						if ptext:
							sections.append({'title': ptext[:60], 'body': ptext})
				# Search sections for query
				for s in sections:
					st = s['title'].lower() + '\n' + s['body'].lower()
					if q in st:
						# simple snippet around first occurrence
						idx = st.find(q)
						start = max(0, idx - 80)
						end = min(len(st), idx + 80)
						snippet = s['body'][start:end].strip() if s['body'] else ''
						# remove Django template tags
						snippet = re.sub(r'{%.*?%}', '', snippet, flags=re.DOTALL)
						snippet = re.sub(r'{{.*?}}', '', snippet, flags=re.DOTALL)
						# highlight the query
						snippet = re.sub(re.escape(q), lambda m: f'<mark>{m.group()}</mark>', snippet, flags=re.IGNORECASE)
						# create an anchor-like slug for per-section links
						slug = re.sub(r"[^a-z0-9]+", '-', s['title'].lower()).strip('-') or 'section'
						results.append({'title': s['title'], 'url': f'/services/#{slug}', 'snippet': snippet, 'source': 'Services'})
			# remove duplicates (by title)
			seen = set()
			unique = []
			for r in results:
				if r['title'] not in seen:
					seen.add(r['title'])
					unique.append(r)
			results = unique
			return render(request, 'main/search_results.html', {'query': query, 'results': results})
		templates_dir = Path(__file__).resolve().parent / 'templates' / 'main'
		if templates_dir.exists():
			for path in templates_dir.glob('*.html'):
				try:
					text = path.read_text(encoding='utf-8')
				except Exception:
					continue
				lower = text.lower()
				name = path.stem
				# Skip the home page as it's not a content page
				if name == 'index':
					continue
				url = '/' if name == 'index' else f'/{name}/'
				_source_map = {
					'markets': 'Markets',
					'projects': 'Projects',
					'services': 'Services',
					'insights': 'Insights',
					'about': 'About',
					'careers': 'Careers',
					'news': 'News',
					'contact': 'Contact',
					'index': 'Home',
				}
				source = _source_map.get(name, name.capitalize())

				# Find <title>
				m_title = re.search(r'<title>(.*?)</title>', text, re.IGNORECASE | re.DOTALL)
				page_title = m_title.group(1).strip() if m_title else source
				# If title contains template syntax, use source instead
				if '{{' in page_title or '{%' in page_title:
					page_title = source

				# Extract headings (h1-h3) with positions for context lookup
				headings = []
				for mh in re.finditer(r'<h([1-3])[^>]*>(.*?)</h\1>', text, re.IGNORECASE | re.DOTALL):
					h_text = re.sub(r'<[^>]+>', '', mh.group(2)).strip()
					# remove Django template tags
					h_text = re.sub(r'\{%.*?%\}', '', h_text, flags=re.DOTALL)
					h_text = re.sub(r'\{\{.*?\}\}', '', h_text, flags=re.DOTALL)
					headings.append({'pos': mh.start(), 'text': html.unescape(h_text)})

				score = 0
				chosen_title = None
				snippet = ''

				# Exact phrase in title tag -> highest relevance
				if q in page_title.lower():
					score += 50
					chosen_title = page_title

				# Search headings first for better contextual results
				for h in headings:
					if q in h['text'].lower():
						score += 40
						chosen_title = h['text']
						# snippet is the heading and small surrounding text
						snippet = h['text']
						# remove Django template tags if any
						snippet = re.sub(r'{%.*?%}', '', snippet, flags=re.DOTALL)
						snippet = re.sub(r'{{.*?}}', '', snippet, flags=re.DOTALL)
						# highlight the query
						snippet = re.sub(re.escape(q), lambda m: f'<mark>{m.group()}</mark>', snippet, flags=re.IGNORECASE)
						break

				# If not matched in headings, search the body
				if chosen_title is None and q in lower:
					# Strip HTML and template tags from the entire text first
					clean_text = re.sub(r'<[^>]+>', '', text)
					clean_text = re.sub(r'{%.*?%}', '', clean_text, flags=re.DOTALL)
					clean_text = re.sub(r'{{.*?}}', '', clean_text, flags=re.DOTALL)
					clean_lower = clean_text.lower()
					idx = clean_lower.find(q)
					if idx != -1:
						# find nearest preceding heading to use as title
						prev_heading = None
						for h in reversed(headings):
							if h['pos'] <= idx:
								prev_heading = h['text']
								break
						if prev_heading and q in prev_heading.lower():
							chosen_title = prev_heading
							score += 30
						else:
							# fall back to page title
							chosen_title = page_title
							score += 10

						# build a snippet around the match in clean text
						start = max(0, idx - 80)
						end = min(len(clean_text), idx + 80)
						snippet = clean_text[start:end].strip()
						# highlight the query in the snippet
						snippet = re.sub(re.escape(q), lambda m: f'<mark>{m.group()}</mark>', snippet, flags=re.IGNORECASE)

				if chosen_title and score > 0:
					results.append({
						'title': html.unescape(chosen_title),
						'url': url,
						'snippet': html.unescape(snippet),
						'source': source,
						'score': score,
					})

			# sort results by score descending, then by title
			results.sort(key=lambda r: (-r.get('score', 0), r.get('title', '')))
			# remove score before returning
			for r in results:
				r.pop('score', None)

		# Also search in PROJECTS data
		for p in PROJECTS:
			# Convert translation proxy objects to strings
			title_str = str(p['title'])
			desc_str = str(p['description'])
			loc_str = str(p['location'])
			p_lower = (title_str + ' ' + desc_str + ' ' + loc_str).lower()
			if q in p_lower:
				idx = p_lower.find(q)
				snippet = desc_str
				# highlight
				snippet = re.sub(re.escape(q), lambda m: f'<mark>{m.group()}</mark>', snippet, flags=re.IGNORECASE)
				results.append({
					'title': title_str,
					'url': '/projects/',
					'snippet': snippet,
					'source': 'Projects',
				})

		# Also search in SERVICES data
		for s in SERVICES:
			# Convert translation proxy objects to strings
			title_str = str(s['title'])
			desc_str = str(s['description'])
			s_lower = (title_str + ' ' + desc_str).lower()
			if q in s_lower:
				idx = s_lower.find(q)
				snippet = desc_str
				# highlight
				snippet = re.sub(re.escape(q), lambda m: f'<mark>{m.group()}</mark>', snippet, flags=re.IGNORECASE)
				results.append({
					'title': title_str,
					'url': '/services/',
					'snippet': snippet,
					'source': 'Services',
				})

	return render(request, 'main/search_results.html', {'query': query, 'results': results})


def architecture_residential(request):
	"""View for Residential/Housing architecture projects."""
	return render(request, 'main/architecture_residential.html')


def architecture_commercial(request):
	"""View for Commercial architecture projects."""
	return render(request, 'main/architecture_commercial.html')


def architecture_hospitality(request):
	"""View for Hospitality/Leisure architecture projects."""
	return render(request, 'main/architecture_hospitality.html')


def architecture_civic(request):
	"""View for Civic architecture projects."""
	return render(request, 'main/architecture_civic.html')
