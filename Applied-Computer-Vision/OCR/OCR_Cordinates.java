package gv_ocr5;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Base64;
import java.util.Iterator;
import java.nio.file.Files;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import okhttp3.MediaType;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.RequestBody;
import okhttp3.Response;

public class OCR_Cordinates {

	public static void main(String[] args) {
		String pathToPNG = "---------png------- path file";
		String gv_key = "------Google API Key-----------";
		String gv_client_id = "---------client id from Service Account KEY JSON file----------";
		String gv_client_secret = "--------------Private key from Service Account KEY JSON file------";
        byte[] pngBytes = null;
		try {
			pngBytes = Files.readAllBytes(Paths.get(pathToPNG));
		} catch (IOException e2) {
			e2.printStackTrace();
		}
        String base64PNG = Base64.getEncoder().encodeToString(pngBytes);
        
        // Code Generated in Postman Desktop
		OkHttpClient client = new OkHttpClient().newBuilder()
				  .build();
				MediaType mediaType = MediaType.parse("application/json");
				RequestBody body = RequestBody.create(mediaType, "{\r\n  \"requests\": [\r\n    {\r\n      \"image\": {\r\n        \"content\": \"" + (String)base64PNG + "\"\r\n      },\r\n      \"features\": [\r\n        {\r\n          \"type\": \"TEXT_DETECTION\"\r\n        }\r\n      ]\r\n    }\r\n  ]\r\n}");
				Request request = new Request.Builder()
				  .url("https://vision.googleapis.com/v1/images:annotate?key=" + gv_key)
				  .method("POST", body)
				  .addHeader("Authorization", "Basic " + gv_client_id + ":" + gv_client_secret)
				  .addHeader("Content-Type", "application/json")
				  .build();

					Response response = null;
					try {
						response = client.newCall(request).execute();
//						System.out.println("Response: " + response.body().string());
					} catch (IOException e1) {
						e1.printStackTrace();
					}
						// Decoding response
						try {
							JSONObject jsonObject = null;
							jsonObject = new JSONObject(response.body().string());
							JSONArray arr = (JSONArray) jsonObject.get("responses");
							JSONObject jsonObject2 = (JSONObject)arr.get(0);			
							JSONArray arr3 = (JSONArray)jsonObject2.get("textAnnotations");
							
							// Iteration over all the Words  
							for(int i = 0; i < arr3.length(); i++) {
								JSONObject jsonObjectDescription = (JSONObject) arr3.get(i);
								System.out.println("description : " + jsonObjectDescription.get("description"));
								JSONObject jsonObjectVertices = (JSONObject)jsonObjectDescription.get("boundingPoly");
								JSONArray arr4 = (JSONArray)jsonObjectVertices.get("vertices");
								
								int left = (int)((JSONObject)arr4.get(0)).get("x");
								int top = (int)((JSONObject)arr4.get(0)).get("y");
								int width = (int)((JSONObject)arr4.get(2)).get("x") - left;
								int height = (int)((JSONObject)arr4.get(2)).get("y") - top;
								System.out.println(left + " " + top + " " + width + " " + height);
							}
							
						} catch (Exception e) {
							e.printStackTrace();
							System.out.println("Exception");
						}
		}
	}