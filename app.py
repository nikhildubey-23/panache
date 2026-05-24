from flask import Flask, render_template, request, jsonify, Response, session, redirect, url_for
import os
from datetime import datetime
from functools import wraps
from werkzeug.security import check_password_hash
from db import query, init_tables, seed_admin, db_available

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'panache-dental-secret-key-change-in-production')

with app.app_context():
    try:
        init_tables()
        seed_admin()
        print("Database initialized successfully")
    except Exception as e:
        print(f"Database init error: {e}")

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'admin_id' not in session:
            return redirect(url_for('admin_login'))
        return f(*args, **kwargs)
    return decorated_function

def get_counts():
    if not db_available():
        return 0, 0, 0
    try:
        bookings = query("SELECT COUNT(*) as c FROM bookings")[0]['c']
        pending = query("SELECT COUNT(*) as c FROM bookings WHERE status = 'pending'")[0]['c']
        unread = query("SELECT COUNT(*) as c FROM contact_messages WHERE status = 'unread'")[0]['c']
        return bookings, pending, unread
    except:
        return 0, 0, 0

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/jaw-fractures')
def jaw_fractures():
    return render_template('jaw_fractures.html')

@app.route('/third-molar-surgery')
def third_molar_surgery():
    return render_template('third_molar_surgery.html')

@app.route('/maxillo-facial-pathology')
def maxillo_facial_pathology():
    return render_template('maxillo_facial_pathology.html')

@app.route('/tmj-surgery')
def tmj_surgery():
    return render_template('tmj_surgery.html')

@app.route('/oral-cancer-surgery')
def oral_cancer_surgery():
    return render_template('oral_cancer_surgery.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/facial-slimming')
def facial_slimming():
    return render_template('facial_slimming.html')

@app.route('/chin-jaw-enhancement')
def chin_jaw_enhancement():
    return render_template('chin_jaw_enhancement.html')

@app.route('/dimpleplasty')
def dimpleplasty():
    return render_template('dimpleplasty.html')

@app.route('/lip-reduction')
def lip_reduction():
    return render_template('lip_reduction.html')

@app.route('/lip-lengthening')
def lip_lengthening():
    return render_template('lip_lengthening.html')

@app.route('/facial-asymmetry')
def facial_asymmetry():
    return render_template('facial_asymmetry.html')

@app.route('/rct')
def rct():
    return render_template('rct.html')

@app.route('/crown-bridges')
def crown_bridges():
    return render_template('crown_bridges.html')

@app.route('/teeth-cleaning')
def teeth_cleaning():
    return render_template('teeth_cleaning.html')

@app.route('/teeth-whitening')
def teeth_whitening():
    return render_template('teethwhitening.html')

@app.route('/extraction')
def extraction():
    return render_template('extraction.html')

@app.route('/composite-restoration')
def composite_restoration():
    return render_template('composite_restoration.html')

@app.route('/digital-dentistry')
def digital_dentistry():
    return render_template('digital_dentistry.html')

@app.route('/digital-smile-design')
def digital_smile_design():
    return render_template('digital_smile_design.html')

@app.route('/crowded-teeth-correction')
def crowded_teeth_correction():
    return render_template('crowded_teeth_correction.html')

@app.route('/minimally-invasive-dentistry')
def minimally_invasive_dentistry():
    return render_template('minimally_invasive_dentistry.html')

@app.route('/painless-injection')
def painless_injection():
    return render_template('painless_injection.html')

@app.route('/invisalign')
def invisalign():
    return render_template('invisalign.html')

@app.route('/laminates-veneers')
def laminates_veneers():
    return render_template('laminates_veneers.html')

@app.route('/all-ceramic-crowns')
def all_ceramic_crowns():
    return render_template('all_ceramic_crowns.html')

@app.route('/dental-implants-missing')
def dental_implants_missing():
    return render_template('dental_implants_missing.html')

@app.route('/full-mouth-implants')
def full_mouth_implants():
    return render_template('full_mouth_implants.html')

@app.route('/gbr')
def gbr():
    return render_template('gbr.html')

@app.route('/malo-bridge')
def malo_bridge():
    return render_template('malo_bridge.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/reviews')
def reviews():
    return render_template('reviews.html')

@app.route('/sitemap.xml')
def sitemap():
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
        {'loc': 'https://www.panachedental.co.in/teeth-whitening', 'priority': '0.7', 'changefreq': 'monthly'},
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
        {'loc': 'https://www.panachedental.co.in/minimally-invasive-dentistry', 'priority': '0.7', 'changefreq': 'monthly'},
        {'loc': 'https://www.panachedental.co.in/painless-injection', 'priority': '0.7', 'changefreq': 'monthly'},
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
    return Response(
        "User-agent: *\nAllow: /\n\nSitemap: https://www.panachedental.co.in/sitemap.xml",
        mimetype='text/plain'
    )

@app.route('/book-appointment', methods=['POST'])
def book_appointment():
    try:
        data = request.get_json() or request.form
        first_name = data.get('firstName')
        last_name = data.get('lastName')
        phone = data.get('phone')
        email = data.get('email')
        appt_date = data.get('date') or data.get('appointmentDate')
        appt_time = data.get('time') or data.get('appointmentTime')
        consult_type = data.get('type') or data.get('consultationType')
        message = data.get('message', '')

        if not all([first_name, last_name, phone, appt_date, appt_time, consult_type]):
            return jsonify({'success': False, 'message': 'Please fill all required fields'}), 400

        query("""
            INSERT INTO bookings (first_name, last_name, phone, email, appointment_date, appointment_time, consultation_type, message)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (first_name, last_name, phone, email, appt_date, appt_time, consult_type, message), fetch=False)

        return jsonify({'success': True, 'message': 'Appointment booked successfully! We will contact you shortly.'})

    except Exception as e:
        print(f"Booking error: {e}")
        return jsonify({'success': False, 'message': 'Error booking appointment. Please try again.'}), 400

@app.route('/send-message', methods=['POST'])
def send_message():
    try:
        data = request.get_json() or request.form
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone', '')
        subject = data.get('subject', '')
        message = data.get('message')

        if not all([name, email, message]):
            return jsonify({'success': False, 'message': 'Please fill name, email and message'}), 400

        query("""
            INSERT INTO contact_messages (name, email, phone, subject, message)
            VALUES (%s, %s, %s, %s, %s)
        """, (name, email, phone, subject, message), fetch=False)

        return jsonify({'success': True, 'message': 'Message sent successfully! We will get back to you soon.'})

    except Exception as e:
        print(f"Message error: {e}")
        return jsonify({'success': False, 'message': 'Error sending message. Please try again.'}), 400

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        if not db_available():
            return render_template('admin_login.html', error='Database not connected. Please set DATABASE_URL in .env file.')
        username = request.form.get('username')
        password = request.form.get('password')
        try:
            users = query("SELECT * FROM admin_users WHERE username = %s", (username,))
            if users and check_password_hash(users[0]['password_hash'], password):
                session['admin_id'] = users[0]['id']
                session['admin_username'] = users[0]['username']
                return redirect(url_for('admin_dashboard'))
        except Exception:
            pass
        return render_template('admin_login.html', error='Invalid username or password')
    return render_template('admin_login.html')

@app.route('/admin/logout')
def admin_logout():
    session.clear()
    return redirect(url_for('admin_login'))

@app.route('/admin')
@login_required
def admin_dashboard():
    total_bookings, pending_bookings, unread_messages = get_counts()
    recent_bookings = []
    recent_messages = []
    if db_available():
        try:
            recent_bookings = query("SELECT * FROM bookings ORDER BY created_at DESC LIMIT 5")
            recent_messages = query("SELECT * FROM contact_messages ORDER BY created_at DESC LIMIT 5")
        except Exception:
            pass
    return render_template('admin_dashboard.html',
        total_bookings=total_bookings,
        pending_bookings=pending_bookings,
        unread_messages=unread_messages,
        recent_bookings=recent_bookings or [],
        recent_messages=recent_messages or []
    )

@app.route('/admin/bookings')
@login_required
def admin_bookings():
    if not db_available():
        return render_template('admin_bookings.html', bookings=[], current_status='')
    status_filter = request.args.get('status', '')
    try:
        if status_filter:
            bookings = query("SELECT * FROM bookings WHERE status = %s ORDER BY created_at DESC", (status_filter,))
        else:
            bookings = query("SELECT * FROM bookings ORDER BY created_at DESC")
    except Exception:
        bookings = []
    return render_template('admin_bookings.html', bookings=bookings, current_status=status_filter)

@app.route('/admin/bookings/<int:booking_id>/status', methods=['POST'])
@login_required
def update_booking_status(booking_id):
    new_status = request.form.get('status')
    query("UPDATE bookings SET status = %s WHERE id = %s", (new_status, booking_id), fetch=False)
    return redirect(url_for('admin_bookings'))

@app.route('/admin/messages')
@login_required
def admin_messages():
    if not db_available():
        return render_template('admin_messages.html', messages=[], current_status='')
    status_filter = request.args.get('status', '')
    try:
        if status_filter:
            messages = query("SELECT * FROM contact_messages WHERE status = %s ORDER BY created_at DESC", (status_filter,))
        else:
            messages = query("SELECT * FROM contact_messages ORDER BY created_at DESC")
    except Exception:
        messages = []
    return render_template('admin_messages.html', messages=messages, current_status=status_filter)

@app.route('/admin/messages/<int:msg_id>/status', methods=['POST'])
@login_required
def update_message_status(msg_id):
    new_status = request.form.get('status')
    query("UPDATE contact_messages SET status = %s WHERE id = %s", (new_status, msg_id), fetch=False)
    return redirect(url_for('admin_messages'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
