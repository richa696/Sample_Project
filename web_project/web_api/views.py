from asyncio.log import logger
import json
from rest_framework.views import APIView
import logging
from rest_framework.response import Response
from rest_framework import status
from .serializers import CryptoCurrencySerializer
from .models import CryptoCurrencyModel
logger = logging.getLogger('django')

# Create your views here.

class SaveOrUpdateData(APIView):
    def post(self,request):
        try:
            cryptoCurrencyData = request.data["data"]
            if cryptoCurrencyData:
                records_to_update = [] #hold the values to insert
                records_to_create = [] #hold the new values alongside existing primary keys to update
                
                # if the records are pre-existing,and add primary keys to the objects
                cryptoCurrencyData = [
                {
                    "id": CryptoCurrencyModel.objects.filter(Name=record.get("Name")).first().id
                    if CryptoCurrencyModel.objects.filter(Name=record.get("Name")).first() is not None else None,
                    **record,
                }
                for record in cryptoCurrencyData
                ]
                
                [
                records_to_update.append(data)
                if data["id"] is not None
                else records_to_create.append(data)
                for data in cryptoCurrencyData
                ]
                
                # Remove the 'id' field, as these will all hold a value of None,since these records do not already exist in the DB
                [record.pop("id") for record in records_to_create]
                
                try: 
                    if records_to_create:
                        is_many = isinstance(cryptoCurrencyData, list)
                        serializer = CryptoCurrencySerializer(data=records_to_create, many=is_many)  
                        if serializer.is_valid():
                            serializer.save()
                            logger.info("-----------------records created successfully--------------")
                            return Response({"status":"success",'status_code': status.HTTP_200_OK})
                        else:
                            logger.error("error occured due to validation failed")
                            logger.error(serializer.errors)
                            return Response({'status':'error','data':serializer.errors, 'status_code':status.HTTP_400_BAD_REQUEST})
                    else:
                        logger.info("---------No new Record found to create-----------")
                    if records_to_update:
                        CryptoCurrencyModel.objects.bulk_update([CryptoCurrencyModel(id=values.get("id"),Name=values.get("Name"),Price=values.get("Price"),_1h=values.get("_1h") ,
                                                                                     _24h=values.get("_24h"),_7d=values.get("_7d"),market_cap=values.get("market_cap"),
                                                                                     volume=values.get("volume"),circulating_supply=values.get("circulating_supply"))
                                                        for values in records_to_update
                                                    ],["Name","Price","_1h","_24h","_7d","market_cap","volume","circulating_supply"],batch_size=100
                                                )
                        logger.info("-----------------records updated successfully--------------")
                        return Response({"status":"success",'status_code': status.HTTP_200_OK})
                    
                    if len(records_to_update) > 0 and len(records_to_create) > 0:
                        logger.info("-----------------No records to create and update --------------")
                        return Response({"status":"success",'status_code': status.HTTP_200_OK})
                    
                except Exception as e:
                    logger.info("--------some exception occured while saving recordes---------"+str(e))
                    return Response({'status':'exception'})
                        
        except Exception as e:
            logger.info("--------some exception occured---------"+str(e))
            return Response({'status':'exception','status_code': status.HTTP_500_INTERNAL_SERVER_ERROR})
            
            
class GetCryptoCurrencyList(APIView):
    def get(self,request):
        try:
            cryptoObjs = CryptoCurrencyModel.objects.all()
            serializer = CryptoCurrencySerializer(cryptoObjs, many=True)
            logger.info("-----------------records fetched successfully--------------")
            return Response({"status":"success","data":serializer.data,'status_code': status.HTTP_200_OK})
        except Exception as e:
            logger.info("--------some exception occured---------"+str(e))
            return Response({'status':'exception','status_code': status.HTTP_500_INTERNAL_SERVER_ERROR})
        