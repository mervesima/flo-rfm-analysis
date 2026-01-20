import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

df_ = pd.read_csv("flo_data_20k.csv")
df = df_.copy()

def create_rfm(dataframe):

    dataframe["total_order"] = (
        dataframe["order_num_total_ever_online"] +
        dataframe["order_num_total_ever_offline"]
    )

    dataframe["total_value"] = (
        dataframe["customer_value_total_ever_online"] +
        dataframe["customer_value_total_ever_offline"]
    )

    date_cols = [col for col in dataframe.columns if "date" in col]
    dataframe[date_cols] = dataframe[date_cols].apply(pd.to_datetime)

    analysis_date = dataframe["last_order_date"].max() + dt.timedelta(days=2)

    rfm = dataframe.groupby("master_id").agg({
        "last_order_date": lambda x: (analysis_date - x.max()).days,
        "total_order": "sum",
        "total_value": "sum"
    })

    rfm.columns = ["recency", "frequency", "monetary"]

    rfm["recency_score"] = pd.qcut(rfm["recency"], 5, labels=[5,4,3,2,1])
    rfm["frequency_score"] = pd.qcut(
        rfm["frequency"].rank(method="first"),
        5,
        labels=[1,2,3,4,5]
    )
    rfm["monetary_score"] = pd.qcut(rfm["monetary"], 5, labels=[1,2,3,4,5])

    rfm["RF_SCORE"] = (
        rfm["recency_score"].astype(str) +
        rfm["frequency_score"].astype(str)
    )

    segment_map = {
        r"[1-2][1-2]": "hibernating",
        r"[1-2][3-4]": "at_risk",
        r"[1-2]5": "cant_loose",
        r"3[1-2]": "about_to_sleep",
        r"33": "need_attention",
        r"[3-4][4-5]": "loyal_customers",
        r"41": "promising",
        r"51": "new_customers",
        r"[4-5][2-3]": "potential_loyalists",
        r"5[4-5]": "champions"
    }

    rfm["segment"] = rfm["RF_SCORE"].replace(segment_map, regex=True)

    return rfm

rfm_result = create_rfm(df)

rfm_result["segment"].value_counts().plot(kind="barh")
plt.title("Müşteri Segment Dağılımı")
plt.xlabel("Müşteri Sayısı")
plt.ylabel("Segment")
plt.savefig("odev_segment_dagilim.png")
plt.show()

rfm_result.head()
