from pydantic import BaseModel


class CellSiteInfo(BaseModel):
    siteId: str
    siteName: str
    location: str
    carrier: str
    siteType: str
    operationalStatus: str
    lastHeartBeat: str
    upTimepercentage: float
    connectionStatus: str
    signalStrength: float
    bandwidth: float
    activeConnection: int
    throughput: float
    errorRate: float
    packetLoss: float
    latency: float
    temperature: float
    powerStatus: str
    batteryLevel: float
    hardwareStatus: str
    activeAlerts: int