from faker import Faker
import random

from models import CellSiteInfo

fake = Faker()


def create_fake_site() -> CellSiteInfo:
    """Generate a fake CellSiteInfo instance using Faker and random values."""
    return CellSiteInfo(
        siteId=fake.uuid4(),
        siteName=fake.company(),
        location=f"{fake.city()}, {fake.country()}",
        carrier=fake.company(),
        siteType=random.choice(["Macro", "Micro", "Small Cell", "Distributed Antenna"]),
        operationalStatus=random.choice(["Operational", "Maintenance", "Down"]),
        lastHeartBeat=fake.iso8601(),
        upTimepercentage=round(random.uniform(90, 100), 2),
        connectionStatus=random.choice(["Connected", "Disconnected"]),
        signalStrength=round(random.uniform(-120, -30), 2),
        bandwidth=round(random.uniform(10, 1000), 2),
        activeConnection=random.randint(0, 1000),
        throughput=round(random.uniform(0.1, 1000), 2),
        errorRate=round(random.uniform(0, 5), 2),
        packetLoss=round(random.uniform(0, 5), 2),
        latency=round(random.uniform(1, 500), 2),
        temperature=round(random.uniform(-20, 50), 2),
        powerStatus=random.choice(["Normal", "Low", "Critical"]),
        batteryLevel=round(random.uniform(0, 100), 2),
        hardwareStatus=random.choice(["OK", "Warning", "Critical"]),
        activeAlerts=random.randint(0, 10),
    )