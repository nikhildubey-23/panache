from flask import Flask, render_template, request, jsonify
import os

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

@app.route('/digital-smile-design')
def digital_smile_design():
    """Render the digital smile design page"""
    return render_template('digital_smile_design.html')

@app.route('/crowded-teeth-correction')
def crowded_teeth_correction():
    """Render the crowded teeth correction page"""
    return render_template('crowded_teeth_correction.html')

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