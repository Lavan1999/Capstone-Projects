   
import streamlit as st
import psycopg2
import pandas as pd
from PIL import Image
import plotly.express as px
        

st.title(':blue[YOUTUBE DATA HARVESTING AND WAREHOUSING]')

st.header(":green[Query Data]")

questions = st.selectbox("Choose your question",
            ("1. Names of all the videos and their channels",
            "2. Channels with most number of videos, and count",
            "3. Top 5 most viewed videos and their channels",
            "4. Comments with each video, and video names",
            "5. Videos with highest likes, and their channel names",
            "6. Total number of likes and dislikes for each video, and video names",
            "7. Total number of views for each channel, and channel names",
            "8. Published videos in the year 2022",
            "9. Average views of all videos in each channel, and channel names",
            "10. videos with highest number of comments, and channel names"))



mydb = psycopg2.connect(
                        host = 'localhost',
                        user = 'postgres',
                        password = 'Lavan123',
                        database = 'youtubedb',
                        port = 5432)
mycursor = mydb.cursor()


if questions == "1. Names of all the videos and their channels":
    query = """
                SELECT video_name, channel_name FROM video_table
            """
    mycursor.execute(query)
    table = mycursor.fetchall()
    df1 = pd.DataFrame(table, columns=["Name of video", "Name of channel"])
    st.header(':violet[Table]')
    st.table(df1)
    

elif questions == "2. Channels with most number of videos, and count":
    query = """    
                SELECT channel_name, COUNT(video_id) AS videocount FROM video_table
                        GROUP BY channel_name ORDER BY videocount DESC LIMIT 1 
            """
    mycursor.execute(query)
    table = mycursor.fetchall()
    df2 = pd.DataFrame(table, columns=["channel name", "video counts"])
    st.header(':violet[Table]')
    st.table(df2)
    

elif questions ==  "3. Top 5 most viewed videos and their channels":
    query = """
                SELECT channel_name, SUM(view_count) as views_count FROM video_table
                GROUP BY channel_name ORDER BY views_count DESC LIMIT 5
            """
    mycursor.execute(query)
    table = mycursor.fetchall()
    df3 = pd.DataFrame(table, columns=["channel name", "view counts"])
    st.header(':violet[Table and visulization]')
    st.table(df3)
    st.header(':violet[Visualization: Top 5 most viewed videos]')
    fig = px.bar(df3,
        x = 'channel name',
        y = 'view counts',
        orientation = 'v'
    )
    st.plotly_chart(fig,use_container_width=True)

    
    

elif questions == "4. Comments with each video, and video names":
    query = """
                SELECT video_table.video_name, SUM(comment_count) as comments_count FROM video_table JOIN comment_table
                    ON (video_id = comment_video_id) GROUP BY video_name ORDER BY comments_count DESC
            """
    mycursor.execute(query)
    table = mycursor.fetchall()
    df4 = pd.DataFrame(table, columns=["video name", "comment counts"])
    st.header(':violet[Table]')
    st.table(df4)
    

elif questions == "5. Videos with highest likes, and their channel names":
    query = """
                SELECT channel_name,video_name, like_count as likes_count FROM video_table
                    ORDER BY likes_count DESC
            """
    mycursor.execute(query)
    table = mycursor.fetchall()
    df5 = pd.DataFrame(table, columns= ["Name of channel","Video name","like counts"])
    st.header(':violet[Visualization: Channels names with highest likes]')
    fig = px.bar(df5,
           y = 'Name of channel',
           x = 'like counts',
           orientation = 'h')
    st.plotly_chart(fig,use_container_width=True)
    st.header(':violet[Table]')
    st.table(df5)
    

elif questions == "6. Total number of likes and dislikes for each video, and video names" :
    query = """
                SELECT video_name, SUM(like_count)as likes_count, SUM(dislike_count) as dislikes_count FROM video_table
                    GROUP BY video_name ORDER BY likes_count DESC
            """
    mycursor.execute(query)
    table = mycursor.fetchall()
    df6 = pd.DataFrame(table, columns=["Name of video", "Likes count","Dislike count"])
    st.header(':violet[Table]')
    st.table(df6)
    

elif questions == "7. Total number of views for each channel, and channel names":
    query = """
                SELECT vt.channel_name, SUM(vt.view_count) as views_count FROM video_table as vt
                GROUP BY vt.channel_name ORDER BY views_count
            """
    mycursor.execute(query)
    table = mycursor.fetchall()
    df7 = pd.DataFrame(table, columns=["Name of Channel", "View Counts"])
    st.header(':violet[Table]')
    st.table(df7)

    
elif questions == "8. Published videos in the year 2022":
    query = """
                 
                    SELECT DISTINCT channel_name FROM video_table
                    WHERE TO_CHAR(published_date, 'YYYY') LIKE '2020%'

            """
    mycursor.execute(query)
    table = mycursor.fetchall()
    df8 = pd.DataFrame(table, columns=["Channel published videos in the year 2022"])
    st.header(':violet[Table]')
    st.table(df8)
    
    
elif questions == "9. Average views of all videos in each channel, and channel names":
    query = """
                SELECT channel_name, ROUND(avg(view_count)) as avg_views FROM video_table
                    GROUP BY channel_name ORDER BY avg_views DESC
            """
    mycursor.execute(query)
    table = mycursor.fetchall()
    df9 = pd.DataFrame(table, columns=["Channel names", "Average views"])
    st.header(':violet[Table and Visulization]')
    st.table(df9)
    st.header(':violet[Visualization: Average views of channels]')
    fig = px.bar(df9,
        y = 'Channel names',
        x = 'Average views',
        orientation = 'h'
    )
    st.plotly_chart(fig,use_container_width=True)
    
    
elif questions == "10. videos with highest number of comments, and channel names":
    query = """
                SELECT channel_name, SUM(comment_count) AS comments_count FROM video_table 
                        GROUP BY channel_name ORDER BY comments_count DESC
            """
    mycursor.execute(query)
    table = mycursor.fetchall()
    df10 = pd.DataFrame(table, columns=["channel name", "comment counts"])
    st.header(':violet[Table and visualization]')
    st.table(df10)
    st.header(':violet[Visualization: Channels comment count]')
    fig = px.bar(df10,
        y = 'channel name',
        x = 'comment counts',
        orientation = 'h'
    )
    st.plotly_chart(fig,use_container_width=True)
