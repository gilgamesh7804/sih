from flask import Flask, render_template, request, jsonify
from scripts.get_city_data import get_city
from scripts.get_hiddengen_data import get_hidden_gem
from scripts.ask import askChatbot
import random
import smtplib
from email.message import EmailMessage

app = Flask(__name__)
otp_storage = {}
# ==================ROUTING=========================
@app.route('/')
def home():
    return render_template('home.html')

@app.route("/city/<string:cityname>")
def city(cityname):
    data = get_city(cityname)
    res = ""
    for i in data.keys():
        res += f"{i} : {data[i]}<br>"
    # return datac
    return render_template(
        "citydesc.html",
        bgimage=data["background_img"],
        ciname=data["cityname"],
        oliner=data["one_liner"],
        history=data["history_info"],
        histp=data["history_1"][0],
        histd=data["history_1"][1],
        sbp=data["scenic_beauty_1"][0],
        sbd=data["scenic_beauty_1"][1],
        spip=data["spiritual_1"][0],
        spid=data["spiritual_1"][1],
        sbi2=data["scenic_beauties_img2"],
        ff1=data["fun_facts1"],
        ff2=data["fun_facts2"],
        ff3=data["fun_facts3"],
        ff4=data["fun_facts4"],
        ff5=data["fun_facts5"],
        hi1=data["historical_img1"],
        sbi1=data["scenic_beauties_img1"],
        spi1=data["spiritual_img1"],
        hi2=data["historical_img2"],
        spi2=data["spiritual_img2"],
        cal=data["calendar"],
        li1=data["event1"],
        li2=data["event2"],
        li3=data["event3"],
    )


@app.route("/hiddengem/<string:placename>")
def hgem(placename):
    data = get_hidden_gem(placename)
    res = ""
    for i in data.keys():
        res += f"{i} : {data[i]}<br>"
    return render_template(
        "hiddengem.html",
        pname=placename,
        hghistory=data["history"],
        hgbg=data["bg_img"],
        hgimg1=data["img1"],
        hgimg2=data["img2"],
        hgimg3=data["img3"],
        ACCESS_KEY="pk.eyJ1IjoiZGFyc2h3aW5zIiwiYSI6ImNtMHFhMzNnZjBiaW0yaXNka3hrZTBtdWMifQ.DZr2iPpvFlHUK6uI7Hb0IQ",
        LAT=data["lat"],
        LNG=data["lng"],
    )


@app.route("/hiddenlist")
def hlist():
    return render_template("hiddenlist.html")

@app.route("/login", methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    if request.method == 'POST':
        data = request.json
        email = data.get('email')

        if not email:
            return jsonify({'error': 'Email is required'}), 400

        # Generate OTP
        otp = ''.join([str(random.randint(0, 9)) for i in range(6)])

        # Send OTP via email
        from_mail = 'shreyanshgupta2020@gmail.com'
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_mail, 'qqcx efwr bzxc npmq')

        msg = EmailMessage()
        msg['Subject'] = "OTP VERIFICATION"
        msg['From'] = from_mail
        msg['To'] = email
        msg.set_content(f"Your OTP is: {otp}")

        server.send_message(msg)
        server.quit()
        print(otp)
        # Store OTP with email
        otp_storage[email] = otp
        return jsonify({'message': 'OTP sent successfully'}), 200

@app.route("/login2", methods=["GET", "POST"])
def login2():
    if request.method == "GET":
        return render_template("login2.html")
    if request.method == "POST":
        data = request.json
        email = data.get('email')
        otp = data.get('otp')
        if(otp_storage[email] == otp):
            return jsonify({'message': 'OTP verified successfully'}), 200
        else:
            return jsonify({'error': 'Invalid OTP'}), 400
@app.route('/apparels')
def apparel():
    return render_template('apparel.html')


@app.route('/dance')
def dance():
    return render_template('dance.html')

@app.route('/music')
def music():
    return render_template('music.html')

@app.route('/festivals/<string:cityname>')
def festival(cityname):
    data = get_city(cityname)
    res = ""
    for i in data.keys():
        res += f"{i} : {data[i]}<br>"
    return render_template('festival.html',
                           festimg1=data["festival_img1"],
                           festimg2=data["festival_img2"],
                           festimg3=data["festival_img3"],
                           festh=data["festival1"][0], 
                           festd=data["festival1"][1],
                           festh2=data["festival2"][0],
                           festd2=data["festival2"][1],
                           festh3=data["festival3"][0],
                           festd3=data["festival3"][1])

@app.route('/food')
def food():
    return render_template('food.html')

@app.route('/attractions/<string:cityname>')
def attractions(cityname):
    data = get_city(cityname)
    res = ""
    for i in data.keys():
        res += f"{i} : {data[i]}<br>"
    return render_template('attraction.html', 
                           ciname2=data["cityname"],
                           att1img1=data["historical_img1"],
                           att1img2=data["historical_img2"],
                           att1img3=data["historical_img3"],
                           att1img4=data["historical_img4"],
                           att1img5=data["historical_img5"],
                           att1img6=data["scenic_beauties_img1"],
                           att1h1=data["history_1"][0],
                           att1h2=data["history_2"][0],
                           att1h3=data["history_3"][0],
                           att1h4=data["history_4"][0],
                           att1h5=data["history_5"][0],
                           att1h6=data["scenic_beauty_1"][0],
                           att1d1=data["history_1"][1],
                           att1d2=data["history_2"][1],
                           att1d3=data["history_3"][1],
                           att1d4=data["history_4"][1],
                           att1d5=data["history_5"][1],
                           att1d6=data["scenic_beauty_1"][1]

                           )

@app.route('/attractions2/<string:cityname>')
def attractions2(cityname):
    data = get_city(cityname)
    res = ""
    for i in data.keys():
        res += f"{i} : {data[i]}<br>"
    return render_template('attraction2.html',
                           ciname3=data["cityname"],
                           attimg1=data["historical_img1"],
                           attimg2=data["historical_img2"],
                           attimg3=data["historical_img3"],
                           attimg4=data["historical_img4"],
                           attimg5=data["historical_img5"],
                           atth1=data["history_1"][0],
                           atth2=data["history_2"][0],
                           atth3=data["history_3"][0],
                           atth4=data["history_4"][0],
                           atth5=data["history_5"][0],
                           attd1=data["history_1"][1],
                           attd2=data["history_2"][1],
                           attd3=data["history_3"][1],
                           attd4=data["history_4"][1],
                           attd5=data["history_5"][1]
                           )

@app.route('/attractions3')
def attraction3():
    return render_template('attraction3.html')

@app.route('/attractions4')
def attractions4():
    return render_template('attraction4.html')

@app.route('/culture/<string:cityname>')
def culture(cityname):
    data = get_city(cityname)
    res = ""
    for i in data.keys():
        res += f"{i} : {data[i]}<br>"
    return render_template('culture.html',
                           artimg1=data["art_img1"],
                           artimg2=data["art_img2"],
                           artimg3=data["art_img3"],
                           arth1=data["art1"][0],
                           arth2=data["art2"][0],
                           arth3=data["art3"][0],
                           artd1=data["art1"][1],
                           artd2=data["art2"][1],
                           artd3=data["art3"][1])
                           
            

@app.route('/citylist')
def citylist():
    return render_template('citylist.html')



@app.route('/chatbot',methods=['GET', 'POST'])
def chatbot():
    if request.method == 'GET':
        return render_template("chatbot.html")
    if request.method == 'POST':
        response = askChatbot(request.json)
        return jsonify({'message': response})

# ==================================================
if __name__ == "__main__":
    app.run()
