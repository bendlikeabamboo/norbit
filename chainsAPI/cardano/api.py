from blockfrost import BlockFrostApi, ApiError, ApiUrls

class cardanoSession:
    def __init__(self):
        self.api = BlockFrostApi(
            project_id='mainnetsf4F40wzudRc9dYvFiHH4aNs2HDl9ZJp',  # or export environment variable BLOCKFROST_PROJECT_ID
            # optional: pass base_url or export BLOCKFROST_API_URL to use testnet, defaults to ApiUrls.mainnet.value
            base_url=ApiUrls.mainnet.value,
        )

    def health(self, return_type="json"):
        return self.api.health(return_type=return_type)
    

x = cardanoSession()
print(x.health())
print(x.api.address(address="addr1vy8lcx87f8udvprnmhah9a9p7p9n3efvq8arxh7uljn543cd34thh"))




