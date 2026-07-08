import { api } from "./api";

export const http = {

  get<T>(url: string) {

    return api<T>(url);
  },

  post<T>(
    url: string,
    body: unknown
  ) {

    return api<T>(
      url,
      {
        method: "POST",
        body,
      }
    );
  },

  patch<T>(
    url: string,
    body: unknown
  ) {

    return api<T>(
      url,
      {
        method: "PATCH",
        body,
      }
    );
  },

  put<T>(
    url: string,
    body: unknown
  ) {

    return api<T>(
      url,
      {
        method: "PUT",
        body,
      }
    );
  },

  delete<T>(
    url: string
  ) {

    return api<T>(
      url,
      {
        method: "DELETE",
      }
    );
  },
};