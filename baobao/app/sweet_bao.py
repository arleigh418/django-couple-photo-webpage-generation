
from calendar import month
from datetime import datetime
from django.contrib.auth.models import User
from django.conf import settings
from django.db import connection
from django.contrib import auth
from django.forms.models import model_to_dict


def generate_sweet_bao_template(cus_data:dict):
	url_of_images = r'C:/baobaoworld/baobao/baobao/media/'
	banner_pic = url_of_images+str(cus_data['banner_pic'])
	left_bao_name = cus_data['left_bao_name']
	left_bao_pic = url_of_images+str(cus_data['left_bao_pic'])
	if not left_bao_pic:
		left_bao_pic ='images/groom.jpg'
	left_bao_ig = cus_data['left_bao_ig']
	if len(str(left_bao_ig))==0:
		left_bao_ig = ''
	else:
		left_bao_ig = f'''
		<a href="{left_bao_ig}"><i class="fa fa-instagram" style="font-size:36px"></i></a>
		'''

	left_bao_des = cus_data['left_bao_des']
	right_bao_name = cus_data['right_bao_name']
	right_bao_pic = url_of_images+str(cus_data['right_bao_pic'])
	if not right_bao_pic:
		right_bao_pic = 'images/bride.jpg'
	right_bao_ig = cus_data['right_bao_ig']
	if len(str(right_bao_ig))==0:
		right_bao_ig = ''
	else:
		right_bao_ig = f'''
		<a href="{right_bao_ig}"><i class="fa fa-instagram" style="font-size:36px"></i></a>
		'''

	right_bao_des = cus_data['right_bao_des']
	bao_together_date = str(cus_data['bao_together_date'])[0:10]
	bao_bao_talk = cus_data['bao_bao_talk']
	bao_thing_title1 = cus_data['bao_big_thing_title1']
	bao_thing_date1 = str(cus_data['bao_big_thing_date1'])[:10]
	bao_thing_des1 = cus_data['bao_big_thing_des1']
	bao_thing_title2 = cus_data['bao_big_thing_title2']
	bao_thing_date2 = str(cus_data['bao_big_thing_date2'])[:10]
	bao_thing_des2 = cus_data['bao_big_thing_des2']
	bao_thing_title3 = cus_data['bao_big_thing_title3']
	bao_thing_date3= str(cus_data['bao_big_thing_date3'])[:10]
	bao_thing_des3 = cus_data['bao_big_thing_des3']
	bao_thing_title4 = cus_data['bao_big_thing_title4']
	bao_thing_date4 = str(cus_data['bao_big_thing_date4'])[:10]
	bao_thing_des4 = cus_data['bao_big_thing_des4']
	
	bao_pic1 = url_of_images+str(cus_data['bao_six_pic1'])
	bao_pic2 = url_of_images+str(cus_data['bao_six_pic2'])
	bao_pic3 = url_of_images+str(cus_data['bao_six_pic3'])
	bao_pic4 = url_of_images+str(cus_data['bao_six_pic4'])
	bao_pic5 = url_of_images+str(cus_data['bao_six_pic5'])
	bao_pic6 = url_of_images+str(cus_data['bao_six_pic6'])


	html_1 = bao_template_region1(left_bao_name=left_bao_name,right_bao_name=right_bao_name)
	html_2 = bao_template_region2(banner_pic = banner_pic,
                                 left_bao_name = left_bao_name,
                                 left_bao_pic = left_bao_pic,
                                 left_bao_des = left_bao_des,
                                 left_bao_ig = left_bao_ig,
                                 right_bao_name = right_bao_name,
                                 right_bao_pic = right_bao_pic,
                                 right_bao_des = right_bao_des,
                                 right_bao_ig = right_bao_ig,
                                 bao_together_date=bao_together_date,
                                 bao_bao_talk=bao_bao_talk)


	html_3 = bao_template_region3(bao_thing_title1=bao_thing_title1, 
                                bao_thing_date1=bao_thing_date1, 
                                bao_thing_des1=bao_thing_des1,
                                bao_thing_title2=bao_thing_title2, 
                                bao_thing_date2=bao_thing_date2, 
                                bao_thing_des2=bao_thing_des2, 
                                bao_thing_title3=bao_thing_title3, 
                                bao_thing_date3 = bao_thing_date3, 
                                bao_thing_des3 = bao_thing_des3, 
                                bao_thing_title4 = bao_thing_title4, 
                                bao_thing_date4 = bao_thing_date4, 
                                bao_thing_des4 = bao_thing_des4)

	html_4 = bao_template_region4(bao_pic1=bao_pic1, 
                                  bao_pic2=bao_pic2, 
                                  bao_pic3=bao_pic3, 
                                  bao_pic4=bao_pic4, 
                                  bao_pic5=bao_pic5, 
                                  bao_pic6=bao_pic6)

	html_5 = bao_template_region5(bao_together_date)
	
	final_html = html_1+html_2+html_3+html_4+html_5
	final_html = final_html.replace('None','     ')
	
	return final_html


def bao_template_region1(left_bao_name,right_bao_name):
    bao_template_region = f'''
	    <!DOCTYPE html>
        <head>
            <meta charset="utf-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <title>Lovely Baobao - {left_bao_name} & {right_bao_name}</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <!-- Facebook and Twitter integration -->
            <meta property="og:title" content="" />
            <meta property="og:image" content="" />
            <meta property="og:url" content="" />
            <meta property="og:site_name" content="" />
            <meta property="og:description" content="" />
            <meta name="twitter:title" content="" />
            <meta name="twitter:image" content="" />
            <meta name="twitter:url" content="" />
            <meta name="twitter:card" content="" />

            <link href='https://fonts.googleapis.com/css?family=Work+Sans:400,300,600,400italic,700' rel='stylesheet' type='text/css'>
            <link href="https://fonts.googleapis.com/css?family=Sacramento" rel="stylesheet">
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
            <!-- Animate.css -->
            <link rel="stylesheet" href="css/animate.css">
            <!-- Icomoon Icon Fonts-->
            <link rel="stylesheet" href="css/icomoon.css">
            <!-- Bootstrap  -->
            <link rel="stylesheet" href="css/bootstrap.css">

            <!-- Magnific Popup -->
            <link rel="stylesheet" href="css/magnific-popup.css">

            <!-- Owl Carousel  -->
            <link rel="stylesheet" href="css/owl.carousel.min.css">
            <link rel="stylesheet" href="css/owl.theme.default.min.css">

            <!-- Theme style  -->
            <link rel="stylesheet" href="css/style.css">

            <!-- Modernizr JS -->
            <script src="js/modernizr-2.6.2.min.js"></script>
            <!-- FOR IE9 below -->
            <!--[if lt IE 9]>
            <script src="js/respond.min.js"></script>
            <![endif]-->

        </head>
        <body>
	'''
    return bao_template_region
    
def bao_template_region2(banner_pic,left_bao_name,left_bao_pic,left_bao_des,left_bao_ig,right_bao_name,right_bao_pic,right_bao_des,right_bao_ig,bao_together_date,bao_bao_talk):
    bao_template_region = f'''
	    <header id="fh5co-header" class="fh5co-cover" role="banner" style="background-image:url({banner_pic});" data-stellar-background-ratio="0.5">
        <div class="overlay"></div>
        <div class="container">
            <div class="row">
                <div class="col-md-8 col-md-offset-2 text-center">
                    <div class="display-t">
                        <div class="display-tc animate-box" data-animate-effect="fadeIn">
                            <h1>{left_bao_name} &amp; {right_bao_name}</h1>
                            <h2>攜手共度</h2>
                            <div class="simply-countdown simply-countdown-countup"></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </header>

    <div id="fh5co-couple">
        <div class="container">
            <div class="row">
                <div class="col-md-8 col-md-offset-2 text-center fh5co-heading animate-box">
                    <h2>Love!</h2>
                    <h3>{bao_together_date}</h3>
                    <p>{bao_bao_talk}</p>
                </div>
            </div>
            <div class="couple-wrap animate-box">
                <div class="couple-half">
                    <div class="groom">
                        <img src="{left_bao_pic}" alt="groom" class="img-responsive">
                    </div>
                    <div class="desc-groom">
                        <h3>{left_bao_name}</h3>
                        <p>{left_bao_des}</p>
                        {left_bao_ig}
                    </div>
                </div>
                <p class="heart text-center"><i class="icon-heart2"></i></p>
                <div class="couple-half">
                    <div class="bride">
                        <img src="{right_bao_pic:}" alt="groom" class="img-responsive">
                    </div>
                    <div class="desc-bride">
                        <h3>{right_bao_name}</h3>
                        <p>{right_bao_des}</p>
                        {right_bao_ig}
                    </div>
                </div>
            </div>
        </div>
    </div>
	'''
    return bao_template_region

def bao_template_region3(bao_thing_title1, bao_thing_date1, bao_thing_des1,bao_thing_title2, bao_thing_date2, bao_thing_des2, bao_thing_title3, bao_thing_date3, bao_thing_des3, bao_thing_title4, bao_thing_date4, bao_thing_des4):
    region = f'''
    <div id="fh5co-couple-story">
		<div class="container">
			<div class="row">
				<div class="col-md-8 col-md-offset-2 text-center fh5co-heading animate-box">
					<span>相親相愛的寶</span>
					<h2>Our Story</h2>
					<p>寶寶攜手共度</p>
				</div>
			</div>
			<div class="row">
				<div class="col-md-12 col-md-offset-0">
					<ul class="timeline animate-box">
    '''

    if  bao_thing_date1 or  bao_thing_title1 or  bao_thing_des1:
        region1 = f'''
        <li class="animate-box">
            <div class="timeline-badge" style="background-image:url(images/couple-1.jpg);"></div>
            <div class="timeline-panel">
                <div class="timeline-heading">
                    <h3 class="timeline-title">{bao_thing_title1}</h3>
                    <span class="date">{bao_thing_date1}</span>
                </div>
                <div class="timeline-body">
                    <p>{bao_thing_des1}</p>
                </div>
            </div>
        </li>
        '''
    else:
        region1 = ''
    
    if  bao_thing_date2 or  bao_thing_title2 or  bao_thing_des2:
        region2 = f'''
        <li class="timeline-inverted animate-box">
            <div class="timeline-badge" style="background-image:url(images/couple-2.jpg);"></div>
            <div class="timeline-panel">
                <div class="timeline-heading">
                    <h3 class="timeline-title">{bao_thing_title2}</h3>
                    <span class="date">{bao_thing_date2}</span>
                </div>
                <div class="timeline-body">
                    <p>{bao_thing_des2}</p>
                </div>
            </div>
        </li>
        '''
    else:
        region2 = ''

    if  bao_thing_date3 or  bao_thing_title3 or  bao_thing_des3:
        region3 = f'''
        <li class="animate-box">
            <div class="timeline-badge" style="background-image:url(images/couple-1.jpg);"></div>
            <div class="timeline-panel">
                <div class="timeline-heading">
                    <h3 class="timeline-title">{bao_thing_title3}</h3>
                    <span class="date">{bao_thing_date3}</span>
                </div>
                <div class="timeline-body">
                    <p>{bao_thing_des3}</p>
                </div>
            </div>
        </li>
        '''
    else:
        region3 = ''
    
    if  bao_thing_date4 or  bao_thing_title4 or  bao_thing_des4:
        region4 = f'''
        <li class="timeline-inverted animate-box">
            <div class="timeline-badge" style="background-image:url(images/couple-2.jpg);"></div>
            <div class="timeline-panel">
                <div class="timeline-heading">
                    <h3 class="timeline-title">{bao_thing_title4}</h3>
                    <span class="date">{bao_thing_date4}</span>
                </div>
                <div class="timeline-body">
                    <p>{bao_thing_des4}</p>
                </div>
            </div>
        </li>
        '''
    else:
        region4 = ''
    
    region5 = '''
    </ul>
				</div>
				
			</div>
		</div>
	</div>
    '''

    if len(region1)==0 and len(region2)==0 and len(region3)==0 and len(region4)==0:
        return region+region5
    else:
        bao_template_region = region+region1+region2+region3+region4+region5
        return bao_template_region
         
def bao_template_region4(bao_pic1, bao_pic2, bao_pic3, bao_pic4, bao_pic5, bao_pic6):
    all_pic = [bao_pic1,bao_pic2,bao_pic3,bao_pic4,bao_pic5,bao_pic6]
    p_store = []
    for all_p in all_pic:
        if all_p:
            p_store.append(all_p)
    region = f'''
    <div id="fh5co-gallery" class="fh5co-section-gray">
		<div class="container">
			<div class="row">
				<div class="col-md-8 col-md-offset-2 text-center fh5co-heading animate-box">
					<span>Our Memories</span>
					<h2>Baobao Lovely pictures</h2>
					<p>閃蝦大家的寶寶照</p>
				</div>
			</div>
			<div class="row row-bottom-padded-md">
				<div class="col-md-12">
					<ul id="fh5co-gallery-list">
    '''

    region1 = ''
    for p in p_store:
        pic_html = f'''
        <li class="one-third animate-box" data-animate-effect="fadeIn" style="background-image: url({p}); ">

                <div class="case-studies-summary">
                    
                </div>
    
        </li>
        '''
        region1 = region1+pic_html

    region2 = '''
    </ul>
                </div>
            </div>
        </div>
    </div>
    '''
    
    bao_template_region = region+region1+region2
    return bao_template_region


def bao_template_region5(bao_together_date):
    now_time = datetime.today()
    year_get = bao_together_date.split('-')[0]
    month_get = bao_together_date.split('-')[1]
    day_get = bao_together_date.split('-')[-1]
    toghther_time = datetime(int(year_get),int(month_get),int(day_get))
    diff_sec = str((now_time-toghther_time).seconds)
    bao_template_1 = f'''
    <div class="gototop js-top">
        <a href="#" class="js-gotop"><i class="icon-arrow-up"></i></a>
    </div>

    <!-- jQuery -->
    <script src="js/jquery.min.js"></script>
    <!-- jQuery Easing -->
    <script src="js/jquery.easing.1.3.js"></script>
    <!-- Bootstrap -->
    <script src="js/bootstrap.min.js"></script>
    <!-- Waypoints -->
    <script src="js/jquery.waypoints.min.js"></script>
    <!-- Carousel -->
    <script src="js/owl.carousel.min.js"></script>
    <!-- countTo -->
    <script src="js/jquery.countTo.js"></script>

    <!-- Stellar -->
    <script src="js/jquery.stellar.min.js"></script>
    <!-- Magnific Popup -->
    <script src="js/jquery.magnific-popup.min.js"></script>
    <script src="js/magnific-popup-options.js"></script>

    <!-- // <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/0.0.1/prism.min.js"></script> -->
    <script src="js/simplyCountdown.js"></script>
    <!-- Main -->
    <script src="js/main.js"></script>

    <script>
    var d = new Date(new Date().getTime() - {diff_sec});
    '''

    bao_template_2 = '''
	// default example
	// direct element injection & Count Up Example
	var countUp = document.querySelector('.simply-countdown-countup');
    simplyCountdown(countUp, {
	year: d.getFullYear(),
	month: d.getMonth(),
	day: d.getDate(),
	countUp: true
    });</script>
    </body>
    </html>
    '''

	
	
    return bao_template_1+bao_template_2
