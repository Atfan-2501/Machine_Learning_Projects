Social Media Sentiment Analysis of the new iPhone 14 series using Azure Logic App

Azure Logic App allows users to fetch new tweets and store these tweets and additional information on the cloud or other third party applications.
This project involves integration of Azure Cognitive Services (Text Analytics) which performs sentiment analysis on the tweets fetched by Azure Logic App. Now the
information of the tweets and the sentiment score is pushed to Azure Sql Database in the SQL server. Finally this data is used to build interactive dashboards on 
PowerBI

The data flow structure is as folllows

![image](https://user-images.githubusercontent.com/102721829/194456065-c05ce404-3e45-4092-9ace-24e2bfc112fb.png)

The below image shows the data flow on the Azure Logic App

![image](https://user-images.githubusercontent.com/102721829/194456437-233e89e0-1a74-417b-87bd-c7b032bcfae6.png)

Finally the data is fetched on the data-visualization tool to track the sentiment of the newly launched iphone 14 series.
