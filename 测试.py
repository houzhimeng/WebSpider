from copyheaders import headers_raw_to_dict
import requests

header = b'''
:authority: www.zhihu.com
:method: GET
:path: /api/v4/articles/35656001/contribute_requests
:scheme: https
accept: */*
accept-encoding: gzip, deflate, br
accept-language: zh-CN,zh;q=0.9,en;q=0.8
cookie: _zap=48356585-ec48-411b-9a66-d487b7ae607b; d_c0="ANDiMph6lw6PTvEQHMMifR0QmejqXGqazZ8=|1543463744"; l_cap_id="MjRjNWNkZDA1YWQ4NDY4MjkxMGRhYzc2OTkyNWZiNDI=|1544601803|6786e6673fe0f040c6a9223f5f4baed9721dc814"; r_cap_id="YmE5MzhmZTIyZTEzNDRmZmE2OTQwZWZjNDRjODNlNDE=|1544601803|815c2e4c7621df052c4f61ed8bfc68b51b758acd"; cap_id="MzM5MzBhMzA5ZGQ0NDkwNTg5MjFjNjkwNDgxZjM0MzA=|1544601803|6cfb19bf6f9133eff82dea3b17141cc2276e9a73"; _xsrf=h29qRM08rAMJXER3FsTSUGeR67a9bAAd; tst=r; capsion_ticket="2|1:0|10:1544685115|14:capsion_ticket|44:MWNiNmVhNzc4NzUzNDJhNDhlZjgyNzk0NjRjMTk1YWM=|727a2ae3d07f83ff43bdceeeef8990f2dc9d0442e52ae6a04b8702f38c716be5"; z_c0="2|1:0|10:1544685155|4:z_c0|92:Mi4xSkxzaEFnQUFBQUFBME9JeW1IcVhEaVlBQUFCZ0FsVk5ZMVRfWEFEUXRBdG1uLTlXQ0hnN2U5TExQUDJYYUNzTW13|d1aa7ab03e3c753f76a5697cb80e08da9d042a909458153bea0eadf0f3a665fa"; q_c1=5136b8abe99a460f941cbd9688908b60|1544960842000|1544960842000; tgw_l7_route=c919f0a0115842464094a26115457122
origin: https://zhuanlan.zhihu.com
referer: https://zhuanlan.zhihu.com/p/35656001
user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36
x-ab-param: top_root=1;top_root_ac=1;top_sj=2;top_bill=0;ls_new_video=1;top_billupdate1=3;top_ebook=0;top_new_user_gift=0;top_recall_tb_short=61;top_v_album=1;se_majorob_style=0;se_prf=0;top_feedre_cpt=101;top_is_gr=0;top_recall_exp_v1=6;top_user_gift=0;top_cc_at=1;top_newuser_feed=0;top_yhgc=0;pf_creator_card=1;se_entity=on;top_gif=0;top_root_web=0;top_vd_gender=0;top_video_score=1;gw_guide=0;ls_is_use_zrec=0;top_ab_validate=3;tp_dis_version=0;top_fqai=2;se_boost=1;top_card=-1;se_search_feed=Y;se_correct_ab=0;se_engine=1;top_30=0;top_billab=0;se_billboardsearch=1;se_ltr_v1=0;top_login_card=1;top_new_user_rec=0;top_f_r_nb=1;top_feedre_itemcf=33;top_feedre=1;ls_topic_is_use_zrec=0;top_new_feed=1;top_recall_core_interest=81;tp_sft=a;se_consulting_price=n;top_follow_reason=0;top_tr=0;top_recall_tb_follow=71;pin_efs=orig;top_mt=0;top_recall_tb_long=51;pin_ef=a;top_feedre_rtt=41;se_backsearch=1;se_consulting_switch=off;se_major_onebox=major;top_no_weighing=1;top_recall_deep_user=1;top_rerank_reformat=2;top_billvideo=0;top_limit_num=0;top_new_video=-1;tp_sticky_android=0;se_websearch=1;top_quality=0;tp_qa_metacard=1;se_ad_index=4;se_auto_syn=0;top_universalebook=1;top_newfollow=0;ls_new_score=1;top_recall_follow_user=91;top_billpic=0;top_recall_tb=5;top_thank=1;zr_art_rec=base;se_gemini_service=content;top_deep_promo=0;top_wonderful=1;soc_brandquestion=1;top_root_few_topic=0;tp_discussion_feed_card_type=2;top_raf=n;se_click2=0;se_filter=0;top_distinction=0;tp_write_pin_guide=3;se_new_market_search=on;top_yc=0;top_ydyq=X;tp_favsku=c;zr_ans_rec=gbrank;se_time_search=origin;se_wiki_box=1;top_test_4_liguangyi=1;top_followtop=1;top_newfollowans=0;top_topic_feedre=21;qa_answerlist_ad=0;se_daxuechuisou=new;se_minor_onebox=d;tp_qa_metacard_top=0;se_mfq=0;top_ntr=1;top_scaled_score=0;top_nad=1;top_root_mg=1;top_rank=0;tp_discussion_feed_type_android=2;top_nucc=3;top_recall=0
x-requested-with: fetch
x-udid: ANDiMph6lw6PTvEQHMMifR0QmejqXGqazZ8='''

header = headers_raw_to_dict(header)
