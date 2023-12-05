/*
 * Selling Partner APIs for Fulfillment Outbound
 * The Selling Partner API for Fulfillment Outbound lets you create applications that help a seller fulfill Multi-Channel Fulfillment orders using their inventory in Amazon's fulfillment network. You can get information on both potential and existing fulfillment orders.
 *
 * OpenAPI spec version: 2020-07-01
 * 
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */


package io.swagger.client.model.fbao;

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import io.swagger.client.model.fbao.FulfillmentOrder;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

/**
 * ListAllFulfillmentOrdersResult
 */
@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2023-10-17T21:02:37.663-07:00")
public class ListAllFulfillmentOrdersResult {
  @SerializedName("nextToken")
  private String nextToken = null;

  @SerializedName("fulfillmentOrders")
  private List<FulfillmentOrder> fulfillmentOrders = null;

  public ListAllFulfillmentOrdersResult nextToken(String nextToken) {
    this.nextToken = nextToken;
    return this;
  }

   /**
   * When present and not empty, pass this string token in the next request to return the next response page.
   * @return nextToken
  **/
  @ApiModelProperty(value = "When present and not empty, pass this string token in the next request to return the next response page.")
  public String getNextToken() {
    return nextToken;
  }

  public void setNextToken(String nextToken) {
    this.nextToken = nextToken;
  }

  public ListAllFulfillmentOrdersResult fulfillmentOrders(List<FulfillmentOrder> fulfillmentOrders) {
    this.fulfillmentOrders = fulfillmentOrders;
    return this;
  }

  public ListAllFulfillmentOrdersResult addFulfillmentOrdersItem(FulfillmentOrder fulfillmentOrdersItem) {
    if (this.fulfillmentOrders == null) {
      this.fulfillmentOrders = new ArrayList<FulfillmentOrder>();
    }
    this.fulfillmentOrders.add(fulfillmentOrdersItem);
    return this;
  }

   /**
   * An array of fulfillment order information.
   * @return fulfillmentOrders
  **/
  @ApiModelProperty(value = "An array of fulfillment order information.")
  public List<FulfillmentOrder> getFulfillmentOrders() {
    return fulfillmentOrders;
  }

  public void setFulfillmentOrders(List<FulfillmentOrder> fulfillmentOrders) {
    this.fulfillmentOrders = fulfillmentOrders;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ListAllFulfillmentOrdersResult listAllFulfillmentOrdersResult = (ListAllFulfillmentOrdersResult) o;
    return Objects.equals(this.nextToken, listAllFulfillmentOrdersResult.nextToken) &&
        Objects.equals(this.fulfillmentOrders, listAllFulfillmentOrdersResult.fulfillmentOrders);
  }

  @Override
  public int hashCode() {
    return Objects.hash(nextToken, fulfillmentOrders);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ListAllFulfillmentOrdersResult {\n");
    
    sb.append("    nextToken: ").append(toIndentedString(nextToken)).append("\n");
    sb.append("    fulfillmentOrders: ").append(toIndentedString(fulfillmentOrders)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(java.lang.Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }

}

