from flask import Flask, render_template, request, jsonify, Response
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    """Render the homepage"""
    return render_template('home.html')

@app.route('/about')
def about():
    """Render the about page"""
    return render_template('about.html')

@app.route('/services')
def services():
    """Render the services page"""
    return render_template('services.html')

@app.route('/jaw-fractures')
def jaw_fractures():
    """Render the jaw fractures page"""
    return render_template('jaw_fractures.html')

@app.route('/third-molar-surgery')
def third_molar_surgery():
    """Render the third molar surgery page"""
    return render_template('third_molar_surgery.html')

@app.route('/maxillo-facial-pathology')
def maxillo_facial_pathology():
    """Render the maxillo facial pathology page"""
    return render_template('maxillo_facial_pathology.html')

@app.route('/tmj-surgery')
def tmj_surgery():
    """Render the TMJ surgery page"""
    return render_template('tmj_surgery.html')

@app.route('/oral-cancer-surgery')
def oral_cancer_surgery():
    """Render the oral cancer surgery page"""
    return render_template('oral_cancer_surgery.html')

@app.route('/contact')
def contact():
    """Render the contact page"""
    return render_template('contact.html')

@app.route('/facial-slimming')
def facial_slimming():
    """Render the facial slimming page"""
    return render_template('facial_slimming.html')

@app.route('/chin-jaw-enhancement')
def chin_jaw_enhancement():
    """Render the chin and jaw line enhancement page"""
    return render_template('chin_jaw_enhancement.html')

@app.route('/dimpleplasty')
def dimpleplasty():
    """Render the dimpleplasty page"""
    return render_template('dimpleplasty.html')

@app.route('/lip-reduction')
def lip_reduction():
    """Render the lip reduction page"""
    return render_template('lip_reduction.html')

@app.route('/lip-lengthening')
def lip_lengthening():
    """Render the lip lengthening page"""
    return render_template('lip_lengthening.html')

@app.route('/facial-asymmetry')
def facial_asymmetry():
    """Render the facial asymmetry correction page"""
    return render_template('facial_asymmetry.html')

@app.route('/rct')
def rct():
    """Render the RCT page"""
    return render_template('rct.html')

@app.route('/crown-bridges')
def crown_bridges():
    """Render the crown and bridges page"""
    return render_template('crown_bridges.html')

@app.route('/teeth-cleaning')
def teeth_cleaning():
    """Render the teeth cleaning page"""
    return render_template('teeth_cleaning.html')

@app.route('/extraction')
def extraction():
    """Render the extraction page"""
    return render_template('extraction.html')

@app.route('/composite-restoration')
def composite_restoration():
    """Render the composite restoration page"""
    return render_template('composite_restoration.html')

@app.route('/digital-dentistry')
def digital_dentistry():
    """Render the digital dentistry page"""
    return render_template('digital_dentistry.html')

@app.route('/digital-smile-design')
def digital_smile_design():
    """Render the digital smile design page"""
    return render_template('digital_smile_design.html')

@app.route('/crowded-teeth-correction')
def crowded_teeth_correction():
    """Render the crowded teeth correction page"""
    return render_template('crowded_teeth_correction.html')

@app.route('/invisalign')
def invisalign():
    """Render the invisalign page"""
    return render_template('invisalign.html')

@app.route('/laminates-veneers')
def laminates_veneers():
    """Render the laminates and veneers page"""
    return render_template('laminates_veneers.html')

@app.route('/all-ceramic-crowns')
def all_ceramic_crowns():
    """Render the all ceramic crowns page"""
    return render_template('all_ceramic_crowns.html')

@app.route('/dental-implants-missing')
def dental_implants_missing():
    """Render the dental implants for missing single tooth page"""
    return render_template('dental_implants_missing.html')

@app.route('/full-mouth-implants')
def full_mouth_implants():
    """Render the full mouth implants page"""
    return render_template('full_mouth_implants.html')

@app.route('/gbr')
def gbr():
    """Render the GBR page"""
    return render_template('gbr.html')

@app.route('/malo-bridge')
def malo_bridge():
    """Render the Malo's Bridge page"""
    return render_template('malo_bridge.html')

@app.route('/gallery')
def gallery():
    """Render the gallery page"""
    return render_template('gallery.html')

@app.route('/reviews')
def reviews():
    """Render the reviews page"""
    return render_template('reviews.html')

@app.route('/sitemap.xml')
def sitemap():
    """Serve sitemap.xml"""
    pages = [
        {'loc': 'https://www.panachedental.co.in/', 'priority': '1.0', 'changefreq': 'weekly'},
        {'loc': 'https://www.panachedental.co.in/about', 'priority': '0.8', 'changefreq': 'monthly'},
        {'loc': 'https://www.panachedental.co.in/services', 'priority': '0.9', 'changefreq': 'monthly'},
        {'loc': 'https://www.panachedental.co.in/contact', 'priority': '0.8', 'changefreq': 'monthly'},
        {'loc': 'https://www.panachedental.co.in/gallery', 'priority': '0.6', 'changefreq': 'monthly'},
        {'loc': 'https://www.panachedental.co.in/reviews', 'priority': '0.6', 'changefreq': 'weekly'},
        {'loc': 'https://www.panachedental.co.in/jaw-fractures', 'priority': '0.7', 'changefreq': 'monthly'},
        {'loc': 'https://www.panachedental.co.in/third-molar-surgery', 'priority': '0.7', 'changefreq': 'monthly'},
        {'loc': 'https://www.panachedental.co.in/maxillo-facial-pathology', 'priority': '0.7', 'changefreq': 'monthly'},
        {'loc': 'https://www.panachedental.co.in/tmj-surgery', 'priority': '0.7', 'changefreq': 'monthly'},
        {'loc': 'https://www.panachedental.co.in/oral-cancer-surgery', 'priority': '0.7', 'changefreq': 'monthly'},
        {'loc': 'https://www.panachedental.co.in/facial-slimming', 'priority': '0.7', 'changefreq': 'monthly'},
        {'loc': 'https://www.panachedental.co.in/chin-jaw-enhancement', 'priority': '0.7', 'changefreq': 'monthly'},
        {'loc': 'https://www.panachedental.co.in/dimpleplasty', 'priority': '0.7', 'changefreq': 'monthly'},
        {'loc': 'https://www.panachedental.co.in/lip-reduction', 'priority': '0.7', 'changefreq': 'monthly'},
        {'loc': 'https://www.panachedental.co.in/lip-lengthening', 'priority': '0.7', 'changefreq': 'monthly'},
        {'loc': 'https://www.panachedental.co.in/facial-asymmetry', 'priority': '0.7', 'changefreq': 'monthly'},
        {'loc': 'https://www.panachedental.co.in/rct', 'priority': '0.7', 'changefreq': 'monthly'},
        {'loc': 'https://www.panachedental.co.in/crown-bridges', 'priority': '0.7', 'changefreq': 'monthly'},
        {'loc': 'https://www.panachedental.co.in/teeth-cleaning', 'priority': '0.7', 'changefreq': 'monthly'},
        {'loc': 'https://www.panachedental.co.in/extraction', 'priority': '0.7', 'changefreq': 'monthly'},
        {'loc': 'https://www.panachedental.co.in/composite-restoration', 'priority': '0.7', 'changefreq': 'monthly'},
        {'loc': 'https://www.panachedental.co.in/digital-dentistry', 'priority': '0.7', 'changefreq': 'monthly'},
        {'loc': 'https://www.panachedental.co.in/digital-smile-design', 'priority': '0.7', 'changefreq': 'monthly'},
        {'loc': 'https://www.panachedental.co.in/crowded-teeth-correction', 'priority': '0.7', 'changefreq': 'monthly'},
        {'loc': 'https://www.panachedental.co.in/invisalign', 'priority': '0.7', 'changefreq': 'monthly'},
        {'loc': 'https://www.panachedental.co.in/laminates-veneers', 'priority': '0.7', 'changefreq': 'monthly'},
        {'loc': 'https://www.panachedental.co.in/all-ceramic-crowns', 'priority': '0.7', 'changefreq': 'monthly'},
        {'loc': 'https://www.panachedental.co.in/dental-implants-missing', 'priority': '0.7', 'changefreq': 'monthly'},
        {'loc': 'https://www.panachedental.co.in/full-mouth-implants', 'priority': '0.7', 'changefreq': 'monthly'},
        {'loc': 'https://www.panachedental.co.in/gbr', 'priority': '0.7', 'changefreq': 'monthly'},
        {'loc': 'https://www.panachedental.co.in/malo-bridge', 'priority': '0.7', 'changefreq': 'monthly'},
    ]
    
    xml = ['<?xml version="1.0" encoding="UTF-8"?>']
    xml.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
    for page in pages:
        xml.append('  <url>')
        xml.append(f'    <loc>{page["loc"]}</loc>')
        xml.append(f'    <changefreq>{page["changefreq"]}</changefreq>')
        xml.append(f'    <priority>{page["priority"]}</priority>')
        xml.append('  </url>')
    xml.append('</urlset>')
    
    return Response('\n'.join(xml), mimetype='application/xml')

@app.route('/robots.txt')
def robots():
    """Serve robots.txt"""
    return Response(
        "User-agent: *\nAllow: /\n\nSitemap: https://www.panachedental.co.in/sitemap.xml",
        mimetype='text/plain'
    )

@app.route('/book-appointment', methods=['POST'])
def book_appointment():
    """Handle appointment booking requests"""
    try:
        # Get form data
        appointment_data = {
            'firstName': request.form.get('firstName'),
            'lastName': request.form.get('lastName'),
            'phone': request.form.get('phone'),
            'email': request.form.get('email'),
            'date': request.form.get('appointmentDate'),
            'time': request.form.get('appointmentTime'),
            'type': request.form.get('consultationType'),
            'message': request.form.get('message')
        }
        
        # Here you would typically:
        # 1. Validate the data
        # 2. Save to database
        # 3. Send confirmation email
        # 4. Send SMS notification
        
        # For now, return success response
        return jsonify({
            'success': True,
            'message': 'Appointment booked successfully! We will contact you shortly.'
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'message': 'Error booking appointment. Please try again.'
        }), 400

# Error handlers for future implementation
# @app.errorhandler(404)
# def not_found(error):
#     """Handle 404 errors"""
#     return render_template('404.html'), 404

# @app.errorhandler(500)
# def internal_error(error):
#     """Handle 500 errors"""
#     return render_template('500.html'), 500

if __name__ == '__main__':
    # Set debug mode for development
    app.run(debug=True, host='0.0.0.0', port=5000)