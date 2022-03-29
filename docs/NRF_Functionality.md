# NRF (Network Repository Function) in 5G

NRF maintains an updated repository of all the 5G elements available in the operator's network along with the services provided by each of the elements in the 5G core. In addition to serving as a repository of the services, the NRF also supports discovery mechanisms that allows 5G elements to discover each other.


![5g_architecture](https://user-images.githubusercontent.com/8631734/160340271-1d2a7d4f-dfd5-40da-b441-5fed76297f4c.png)

The NRF interacts with every other element in the 5G core network and it supports "Management Services" and "Discovery Services".

## NRF Management Services
The NRF Management service is identified by the service operation name Nnrf_NFManagement.
NRF supports the following management services:

1. Register NF instance (NFRegister): Allows an NF instance to register its NF profile in the NRF along with the list of services provided by the NF     instance.
2. Update NF instance (NFUpdate): Enables an NF instance to partially update or replace the parameters of its NF profile in the NRF. It also allows to add    or delete services provided by the NF instance.
   This operation supports the following:
- Complete Replacement of NF profile
- Add, Remove, or Update attributes of NF Profile
- Heart beat & Load info of NF
3. De-register NF instance (NFDeregister): Enables an NF instance to de-register its NF profile and the services provided by the NF instance from the 5G  network.
4. Subscribe to Status (NFStatusSubscribe): Enables an NF instance to subscribe the status changes of other NF instances registered in the NRF.
5. Unsubscribe to Status (NFStatusUnsubscribe): Enables an NF instance to unsubscribe the status changes of other NF instances.
6. Receive Notifications of Status (NFStatusNotify): Enables the NRF to notify changes in status of NF instances to any subscriber of NF status. Changes also include information regarding newly registered and de-registered NFs.

## Discovery Service

The NRF Discovery service is identified by the service operation name Nnrf_NFDiscovery Service.
NRF supports the following Discovery service:

1. Discover NF instance (NFDiscover): NRF supports discovery of the IP address/FQDN of the NF instances, or NF Services that match certain input criteria.



